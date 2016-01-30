from django.conf.urls import patterns, url

from .rest import base_search


urlpatterns = patterns(
    '',
    url(r'^api/base_search/$', base_search, name='base_search'),
)