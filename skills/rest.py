from rest_framework import viewsets
from rest_framework.filters import SearchFilter, DjangoFilterBackend

from .serializers import SkillSerializer, UserSkillSerializer, SupportUserSkillSerializer
from .models import Skill, UserSkill, SupportUserSkill



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
    """
    serializer_class = UserSkillSerializer
    queryset = UserSkill.objects.all()
    filter_fields = ('user', 'skill')


class SupportUserSkillViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    """
    serializer_class = SupportUserSkillSerializer
    queryset = SupportUserSkill.objects.all()
    filter_fields = ('supporter', 'user_skill')
