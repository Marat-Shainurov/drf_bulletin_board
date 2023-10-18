from django.urls import path

from ads.apps import AdsConfig
from ads.views.ad import AdListView, AdCreateView, AdRetrieveView, AdUpdateView, AdDeleteView

app_name = AdsConfig.name

urlpatterns = [
    # ads
    path('ads/', AdListView.as_view(), name='ads_list'),
    path('ads/create/', AdCreateView.as_view(), name='ads_create'),
    path('ads/get/<int:pk>/', AdRetrieveView.as_view(), name='ads_get'),
    path('ads/update/<int:pk>/', AdUpdateView.as_view(), name='ads_update'),
    path('ads/delete/<int:pk>/', AdDeleteView.as_view(), name='ads_delete'),

    # reviews
]
