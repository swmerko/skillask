from django.conf.urls import url

from .views import add_skills

urlpatterns = [
    url(r'^add-skills$', add_skills, name='add_skills'),
]
