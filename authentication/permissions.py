from rest_framework import permissions


class UserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Just authenticated superuser can see list of users
        if view.action == 'list':
            return request.user.is_authenticated and request.user.is_superuser

        # Creating user doesn't need authentication
        elif view.action == 'create':
            return True

        # Returning True for objects changes for now but check it in has_object_permission method
        elif view.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):
        # Deny actions on objects if the user is not authenticated
        if not request.user.is_authenticated:
            return False

        # SuperUser can do anything but another users just can GET/DELETE/PUT/PATCH/DELETE themselves
        if view.action == 'retrieve':
            return obj == request.user or request.user.is_superuser
        elif view.action in ['update', 'partial_update']:
            return obj == request.user or request.user.is_superuser
        elif view.action == 'destroy':
            return obj == request.user or request.user.is_superuser
        else:
            return False
