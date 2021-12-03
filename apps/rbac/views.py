from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from apps.user.models import User
from django.contrib.auth.models import Group, Permission
from .serializers import UserGroupSerializer, UserSerializer, GroupSerializer, PermissionSerializer

from django.conf import settings

class UserViewSet(ModelViewSet):
    permission_classes = []
    queryset = User.objects
    serializer_class = UserSerializer

    @action(methods=["post"], detail=True, url_path="usegroup")
    def use_group(self, request, pk, **kwargs):
        user = self.request.user
        serializer = UserGroupSerializer(data=request.data)
        serializer.is_valid()
        group_id = serializer.validated_data["group"]
        print(settings.AUTHENTICATION_BACKENDS)
        try:
            group  = user.groups.get(id=group_id)
        except (ObjectDoesNotExist, MultipleObjectsReturned) as e:
            return Response(data={"message": "切换失败"})
        else:
            request.session["group"] = {"id": group.id, "name": group.name}
            return Response(data={"message": "切换成功"})


class GroupViewSet(ModelViewSet):
    permission_classes = []
    queryset = Group.objects
    serializer_class = GroupSerializer


class PermissionViewSet(ModelViewSet):
    permission_classes = []
    queryset = Permission.objects
    serializer_class = PermissionSerializer