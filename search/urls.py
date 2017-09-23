from django.conf.urls import url

from .views import search
from .rest import base_search

urlpatterns = [
    url(r'^api/base_search/$', base_search, name='base_search'),
    url(r'^$', search, name='search'),
    url(r'^(?P<skill_id>\d+)$', search, name='search_skill_id'),
]
