from django.conf.urls import url

from .views import add_skills, add_skill

urlpatterns = [
    url(r'^add-skills/$', add_skills, name='add_skills'),
    url(r'^add-skills/(?P<skill_id>\d+)$', add_skill, name='add_skill'),
]
