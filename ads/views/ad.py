from rest_framework import generics

from ads.models import Ad
from ads.serializers import AdCreateUpdateSerializer, AdBaseSerializer


class AdCreateView(generics.CreateAPIView):
    serializer_class = AdCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdRetrieveView(generics.RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdBaseSerializer


class AdListView(generics.ListAPIView):
    serializer_class = AdBaseSerializer
    queryset = Ad.objects.all()


class AdUpdateView(generics.UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateUpdateSerializer


class AdDeleteView(generics.DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdBaseSerializer
