from rest_framework import serializers

from ads.models import Ad
from ads.serializers import ReviewBaseSerializer
from users.serializers import CustomUserShort


class AdCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('title', 'price', 'description', 'preview',)


class AdBaseSerializer(serializers.ModelSerializer):
    author = CustomUserShort()
    ad_reviews = ReviewBaseSerializer(many=True, read_only=True)

    class Meta:
        model = Ad
        fields = ('id', 'title', 'price', 'description', 'preview', 'author', 'created_at', 'ad_reviews',)


class AdSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ('id', 'title', 'price',)
