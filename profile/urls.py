from django.conf.urls import url
from django.views.generic import RedirectView

from .views import add_skills, add_skill, public_profile

urlpatterns = [
    url(r'^add-skills/$', add_skills, name='add_skills'),
    url(r'^add-skills/(?P<skill_id>\d+)$', add_skill, name='add_skill'),
    url(r'^public/(?P<user_id>\d+)$', public_profile, name='public_profile'),
    url(r'^profile$', RedirectView.as_view(pattern_name='add_skills', permanent=False), name='private_profile'),
]
