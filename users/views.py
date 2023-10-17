from rest_framework import viewsets

from users.models import CustomUser
from users.serializers import CustomUserCreateSerializer, CustomerUserBaseSerializer, CustomUserUpdateSerializer


class CustomerUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == 'POST':
            return CustomUserCreateSerializer
        if self.request.method == 'PUT':
            return CustomUserUpdateSerializer
        if self.request.method == 'PATCH':
            return CustomUserUpdateSerializer
        else:
            return CustomerUserBaseSerializer
