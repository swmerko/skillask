from django.conf.urls import url
from .rest import base_search

urlpatterns = [
    url(r'^api/base_search/$', base_search, name='base_search'),
]
