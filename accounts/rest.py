from rest_framework import viewsets

from .serializers import UserProfileSerializer
from .models import UserProfile


class UserProfileViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the accounts
    associated with the user.
    """
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
