# Create your views here.
from django.core.urlresolvers import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class APIList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response({
            'accounts': request.build_absolute_uri('/accounts/api/'),
            'skills': request.build_absolute_uri('/skills/api/'),
            'search': request.build_absolute_uri(reverse('base_search')),
        })
