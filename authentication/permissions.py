from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        return (
            user.is_authenticated and
            getattr(user, 'role', None) == 'admin'
        )


class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        return (
            user.is_authenticated and
            getattr(user, 'role', None) == 'doctor'
        )


class IsPatient(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        return (
            user.is_authenticated and
            getattr(user, 'role', None) == 'patient'
        )


class IsPatientOrAdmin(BasePermission):
        def has_permission(self, request, view):
            return (request.user.is_authenticated and (request.user.role == 'patient' or request.user.role == 'admin'))

