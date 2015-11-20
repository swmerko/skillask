from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

from .views import APIList

urlpatterns = [
    url(r'^$', login_required(APIList.as_view())),
]
