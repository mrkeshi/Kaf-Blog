from rest_framework import permissions

class IsAdminOrReadCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action in ["list", "retrieve", "create"]:
            return True
        return bool(request.user and request.user.is_staff)
