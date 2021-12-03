from . import views
from rest_framework.urls import path
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('token', obtain_jwt_token)
]