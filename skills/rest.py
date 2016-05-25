from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError
from rest_framework.filters import SearchFilter, DjangoFilterBackend
from rest_framework.response import Response
from .models import Skill, UserSkill, SupportUserSkill, SkillProposal
from .serializers import SkillSerializer, UserSkillSerializer, SupportUserSkillSerializer, UserSkillExtendedSerializer, \
    SkillProposalSerializer, CreateSkillSerializer, CreateSkillProposalSerializer


# class SkillFilter(django_filters.FilterSet):
#     name__icontains = django_filters.NumberFilter(name="price", lookup_type='icontains')
#
#     class Meta:
#         model = Skill
#         fields = ('name', 'name__icontains', 'slug')


class SkillViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    """
    serializer_class = SkillSerializer
    queryset = Skill.objects.all()
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filter_fields = ('name', 'slug', 'category')
    search_fields = ('name',)

    def get_serializer_class(self):
        if self.action in ['create']:
            return CreateSkillSerializer
        else:
            return SkillSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Skill.objects.all()
        exclude_their_skills = self.request.query_params.get('excludeTheirSkills', 'false')
        exclude_their_skills = exclude_their_skills in ['y', 'yes', 'true', '1']
        if exclude_their_skills:
            their_skill_list = UserSkill.objects.filter(user_id=self.request.user.id).values_list('skill_id', flat=True)
            queryset = queryset.exclude(id__in=their_skill_list)
        return queryset

    def create(self, request, *args, **kwargs):
        raise ValidationError('Use skill proposal instead!')


class UserSkillViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.

    Querystring Parameters:
    **skillId**
    """

    filter_fields = ('id',)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = UserSkill.objects.all()
        skill_id = self.request.query_params.get('skillId', None)
        if skill_id is not None:
            queryset = queryset.filter(skill_id=skill_id)

        user_id = self.request.query_params.get('userId', None)
        if user_id:
            queryset = queryset.filter(user_id=user_id)

        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return UserSkillExtendedSerializer
        else:
            return UserSkillSerializer

    def delete(self, request, pk, format=None):
            snippet = self.get_object(pk)
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT, content_type='application/json')

class SupportUserSkillViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    """
    serializer_class = SupportUserSkillSerializer
    queryset = SupportUserSkill.objects.all()
    filter_fields = ('supporter', 'user_skill')


class SkillProposalViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the proposal
    associated with the skill.
    """
    serializer_class = SkillProposalSerializer
    queryset = SkillProposal.objects.all()
    filter_fields = ('closed', 'skill', 'user', 'moderator')

    def get_serializer_class(self):
        if self.action in ['create']:
            return CreateSkillProposalSerializer
        else:
            return SkillProposalSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            proposal_node = Skill.objects.get(pk=1)
            if proposal_node.slug != 'proposals':
                proposal_node.slug = 'proposals'
                proposal_node.name = 'proposals'
        except Skill.DoesNotExist:
            proposal_node = Skill.add_root(name='proposals', slug='proposals', pk=1)
        proposal_data = serializer.data

        # state 1 is pending
        new_skill = proposal_node.add_child(name=proposal_data['name'],
                                            slug=proposal_data['name'],
                                            enabled=True,
                                            state=1)
        proposed_skill = SkillProposal.objects.create(
            user=request.user,
            skill=new_skill
        )

        if proposal_data['add_skill_to_user']:
            UserSkill.objects.create(user=request.user, skill=new_skill)

        serializer = SkillProposalSerializer(proposed_skill)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
