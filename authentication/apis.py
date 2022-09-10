from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser

from authentication.models import User
from authentication.permissions import UserPermission
from authentication.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    # User ModelViewSet used to have all HTTP methods(GET, POST, PUT, PATCH, DELETE) for User objects as api
    authentication_classes = [BasicAuthentication]
    permission_classes = [UserPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer
