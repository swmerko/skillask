from rest_framework import routers
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from skills.rest import SkillViewSet, UserSkillViewSet, SupportUserSkillViewSet

router = DefaultRouter('skills')

router.register(r'skills', SkillViewSet, base_name='skill')
router.register(r'user_skills', UserSkillViewSet, base_name='user_skill')
router.register(r'support_user_skills', SupportUserSkillViewSet, base_name='support_user_skill')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]