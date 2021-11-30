from rest_framework.serializers import ModelSerializer
from .models import System

class SystemSerializer(ModelSerializer):

    class Meta:
        model = System
        fields = "__all__"