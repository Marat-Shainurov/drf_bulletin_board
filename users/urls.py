from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import CustomerUserViewSet

app_name = UsersConfig.name

urlpatterns = []

router = DefaultRouter()
router.register('users', CustomerUserViewSet, basename='users')

urlpatterns += router.urls
