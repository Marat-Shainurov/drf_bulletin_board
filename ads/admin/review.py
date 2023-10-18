from django.contrib import admin
from django.contrib.admin import ModelAdmin

from ads.models import Review


@admin.register(Review)
class AdminReview(ModelAdmin):
    list_display = ('id', 'author', 'ad', 'created_at',)
    list_filter = ('author', 'ad',)
    search_fields = ('id',)
