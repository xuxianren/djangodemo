from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from django.middleware.csrf import CsrfViewMiddleware
class LoginView(APIView):
    permission_classes = []
    
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            return Response(data={"message": "登录成功"})
        else:
            return Response(data={"message": "登录失败, 请校验用户名或者密码"})


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response(data={"message": "登出成功"})
