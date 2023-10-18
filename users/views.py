from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

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

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
