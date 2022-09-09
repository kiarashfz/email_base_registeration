from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authentication.apis import UserViewSet

router = DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
