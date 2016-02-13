from django.conf.urls import include, url
from rest_framework import routers

from accounts.rest import UserProfileViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'user', UserViewSet, base_name='user')
router.register(r'user_profile', UserProfileViewSet, base_name='user_profile')


urlpatterns = [
    url(r'^api/', include(router.urls)),
]
