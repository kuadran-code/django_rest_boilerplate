from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializers(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.CharField()

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def create(self, **kwargs):
        user = User.objects.create_user(**self.validated_data)
        print(user)
        return user
