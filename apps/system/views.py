from rest_framework.viewsets import ModelViewSet
from .serializers import SystemSerializer
from .models import System
from django.middleware.csrf import CsrfViewMiddleware
class SystemViewSet(ModelViewSet):

    queryset = System.objects
    serializer_class = SystemSerializer
    