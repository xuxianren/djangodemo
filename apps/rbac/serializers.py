from re import L
from django.db import models
from django.db.models import fields
from rest_framework.serializers import Serializer, ModelSerializer
from django.contrib.auth.models import Group, Permission
from rest_framework import serializers
from apps.user.models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(ModelSerializer):
    
    def validate_password(self, value):
        return make_password(value)

    class Meta:
        model = User
        exclude = ("first_name", "last_name")
        extra_kwargs = {
            'password': {'write_only': True},
            'date_joined': {'read_only': True},
            'last_login': {'read_only': True},
        }

class UserGroupSerializer(Serializer):
    group = serializers.IntegerField()
    

class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"

class PermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"