from rest_framework import generics

from ads.models import Review
from ads.serializers import ReviewCreateUpdateSerializer, ReviewBaseSerializer


class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewCreateUpdateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ReviewRetrieveView(generics.RetrieveAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewBaseSerializer


class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewBaseSerializer
    queryset = Review.objects.all()


class ReviewUpdateView(generics.UpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateUpdateSerializer


class ReviewDeleteView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewBaseSerializer
