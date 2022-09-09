from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Email Base Registration",
        default_version="v1",
        description="An API for Managing Users",
        terms_of_service="https://github.com/kiarashfz/",
        contact=openapi.Contact(email="kiawfz3673@gmail.com"),
        license=openapi.License(name="KiarashFz License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
