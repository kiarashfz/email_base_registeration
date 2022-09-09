from rest_framework import viewsets

from authentication.models import User
from authentication.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    User ModelViewSet used to have all HTTP methods(GET, POST, PUT, PATCH, DELETE) for User objects as api
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
