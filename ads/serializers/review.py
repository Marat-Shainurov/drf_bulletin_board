from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from ads.models import Review


class ReviewCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('text', 'ad',)


class ReviewBaseSerializer(serializers.ModelSerializer):
    text = SerializerMethodField()

    class Meta:
        model = Review
        fields = ('id', 'ad', 'created_at', 'text')

    @staticmethod
    def get_text(review):
        return f'{review.text[0:9]}...' if len(review.text) > 10 else review.text
