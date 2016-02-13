from django.contrib.auth.models import User
from rest_framework import viewsets

from .serializers import UserProfileSerializer, UserSerializer
from .models import UserProfile


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    """
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        get_current_user = self.kwargs.get('pk', None) == 'current'
        if get_current_user:
            return User.objects.get(pk=self.request.user.pk)
        else:
            return super(UserViewSet, self).get_object()
