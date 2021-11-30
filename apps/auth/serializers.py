from rest_framework.serializers import Serializer, CharField

class LoginSerializer(Serializer):
    username = CharField("用户名称", max_length=20)
    password = CharField("用户密码", max_length=20)
