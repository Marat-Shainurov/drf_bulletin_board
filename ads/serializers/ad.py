from rest_framework import serializers

from ads.models import Ad
from users.serializers import CustomUserShort


class AdCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('title', 'price', 'description',)


class AdBaseSerializer(serializers.ModelSerializer):
    author = CustomUserShort()

    class Meta:
        model = Ad
        fields = ('id', 'title', 'price', 'description', 'author', 'created_at',)


class AdSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('id', 'title', 'price',)
