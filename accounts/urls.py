from django.conf.urls import include, url
from rest_framework import routers

from .rest import UserProfileViewSet, UserViewSet
from .views import post_social_login, post_social_registration

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='users')
router.register(r'user_profiles', UserProfileViewSet, base_name='user_profiles')


urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^post-social-login/', post_social_login, name='post_social_login'),
    url(r'^post-social-registration/', post_social_registration, name='post_social_registration'),

]
