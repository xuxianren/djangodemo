from rest_framework.viewsets import ModelViewSet
from .serializers import SystemSerializer
from .models import System
from django.middleware.csrf import CsrfViewMiddleware
from rest_framework.permissions import BasePermission 

class SystemViewSet(ModelViewSet):

    queryset = System.objects
    serializer_class = SystemSerializer

    def retrieve(self, request, *args, **kwargs):
        # print(request.COOKIES.get("role"))
        # print(request.session.items())
        # print(request.get_signed_cookie("role"))
        resp = super().retrieve(request, *args, **kwargs)
        # resp.set_signed_cookie("role", 1) # 加盐的cookie
        return resp