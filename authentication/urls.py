from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authentication.apis import UserViewSet
from django.conf.urls import url

from authentication.views import schema_view

router = DefaultRouter()
router.register('', UserViewSet)

urlpatterns = [
    path('users/', include(router.urls)),
    url(r'^$', schema_view)
]
