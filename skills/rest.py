from rest_framework import viewsets
from rest_framework.filters import SearchFilter, DjangoFilterBackend
from .models import Skill, UserSkill, SupportUserSkill
from .serializers import SkillSerializer, UserSkillSerializer, SupportUserSkillSerializer, UserSkillExtendedSerializer


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
    filter_fields = ('name', 'slug')
    search_fields = ('name',)


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

        user_id = self.request.query_params.get('skillId', None)
        if user_id:
            queryset = queryset.filter(user_id=user_id)

        return queryset

    def get_serializer_class(self):
        if self.action == 'list':
            return UserSkillExtendedSerializer
        else:
            return UserSkillSerializer


class SupportUserSkillViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    """
    serializer_class = SupportUserSkillSerializer
    queryset = SupportUserSkill.objects.all()
    filter_fields = ('supporter', 'user_skill')
