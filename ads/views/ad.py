from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ads.models import Ad
from ads.pagination import BulletinBoardPagination
from ads.permissions import IsOwner
from ads.serializers import AdCreateUpdateSerializer, AdBaseSerializer


class AdCreateView(generics.CreateAPIView):
    serializer_class = AdCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdRetrieveView(generics.RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdBaseSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]


class AdListView(generics.ListAPIView):
    serializer_class = AdBaseSerializer
    queryset = Ad.objects.all()
    pagination_class = BulletinBoardPagination


class AdUpdateView(generics.UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]


class AdDeleteView(generics.DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdBaseSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]
