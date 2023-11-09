from django.contrib import admin
from django.contrib.admin import ModelAdmin

from ads.models import Ad


@admin.register(Ad)
class AdminAd(ModelAdmin):
    list_display = ('id', 'title', 'price', 'author', 'created_at', 'preview',)
    list_filter = ('author', 'price',)
    search_fields = ('id', 'title',)
