from django.urls import path

from ads.apps import AdsConfig
from ads.views import (AdListView, AdCreateView, AdRetrieveView, AdUpdateView, AdDeleteView, ReviewListView,
                       ReviewDeleteView, ReviewCreateView, ReviewUpdateView, ReviewRetrieveView)

app_name = AdsConfig.name

urlpatterns = [
    # ads
    path('ads/', AdListView.as_view(), name='ads_list'),
    path('ads/create/', AdCreateView.as_view(), name='ads_create'),
    path('ads/get/<int:pk>/', AdRetrieveView.as_view(), name='ads_get'),
    path('ads/update/<int:pk>/', AdUpdateView.as_view(), name='ads_update'),
    path('ads/delete/<int:pk>/', AdDeleteView.as_view(), name='ads_delete'),

    # reviews
    path('reviews/', ReviewListView.as_view(), name='reviews_list'),
    path('reviews/create/', ReviewCreateView.as_view(), name='reviews_create'),
    path('reviews/get/<int:pk>/', ReviewRetrieveView.as_view(), name='reviews_get'),
    path('reviews/update/<int:pk>/', ReviewUpdateView.as_view(), name='reviews_update'),
    path('reviews/delete/<int:pk>/', ReviewDeleteView.as_view(), name='reviews_delete'),
]
