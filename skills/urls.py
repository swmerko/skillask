from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from .rest import SkillViewSet, UserSkillViewSet, SupportUserSkillViewSet, SkillProposalViewSet

router = DefaultRouter('skills')

router.register(r'skills', SkillViewSet, base_name='skill')
router.register(r'skill_proposals', SkillProposalViewSet, base_name='skill_proposals')
router.register(r'user_skills', UserSkillViewSet, base_name='user_skill')
router.register(r'support_user_skills', SupportUserSkillViewSet, base_name='support_user_skill')

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
