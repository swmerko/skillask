from django.conf.urls import url

from .views import add_skills, add_skill, public_profile

urlpatterns = [
    url(r'^add-skills/$', add_skills, name='add_skills'),
    url(r'^add-skills/(?P<skill_id>\d+)$', add_skill, name='add_skill'),
    url(r'^public/(?P<user_id>\d+)$', public_profile, name='public_profile'),
]
