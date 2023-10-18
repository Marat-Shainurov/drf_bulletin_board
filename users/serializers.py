from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from users.models import CustomUser


class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email", "phone_number", "password",)

    @staticmethod
    def validate_password(value: str) -> str:
        return make_password(value)


class CustomerUserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "phone_number", "is_staff", "is_superuser", "is_active")


class CustomUserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("email", "phone_number", "is_staff", "is_active")
