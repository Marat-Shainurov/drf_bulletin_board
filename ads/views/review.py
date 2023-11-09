from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ads.models import Review
from ads.pagination import BulletinBoardPagination
from ads.permissions import IsOwner
from ads.serializers import ReviewCreateUpdateSerializer, ReviewBaseSerializer


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReviewRetrieveView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewBaseSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]


class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewBaseSerializer
    queryset = Review.objects.all()
    pagination_class = BulletinBoardPagination
    permission_classes = [IsAuthenticated]


class ReviewUpdateView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]


class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewBaseSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]
