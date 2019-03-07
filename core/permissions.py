from rest_framework import permissions

class SuperUserPermission(permissions.BasePermission):
    message = 'Restricted Information'

    def has_permission(self, request, view):
        return request.user.is_superuser
