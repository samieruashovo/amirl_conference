from rest_framework import permissions


class ConferencePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        # If it's a safe method (GET, HEAD, OPTIONS), allow everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        else:
            return request.user in obj.organizers.all()
