from django.conf.urls import include, url
from rest_framework import routers

from accounts.rest import UserProfileViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'user_profiles', UserProfileViewSet, base_name='user_profiles')


urlpatterns = [
    url(r'^api/', include(router.urls)),
]
