from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication

from authentication.models import User
from authentication.permissions import UserPermission
from authentication.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    # User ModelViewSet used to have all HTTP methods(GET, POST, PUT, PATCH, DELETE) for User objects as api
    authentication_classes = [BasicAuthentication]
    permission_classes = [UserPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @swagger_auto_schema(operation_description="Superuser have access to users list.")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Each user can see own object. Superuser have access to see all users.")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Each user can delete own object. Superuser have access to delete all users.")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Each user can update own object. Superuser have access to update all users.")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Each user can update own object. Superuser have access to update all users.")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
