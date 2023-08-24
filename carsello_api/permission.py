from rest_framework import permissions


class SuperuserOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return False

class OrderPostOnly(permissions.BasePermission):
    edit_methods = {"POST"}
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        if request.method in self.edit_methods:
            return True
        return False

class AllowSafe(permissions.BasePermission):
    # @user_passes_test(lambda u: u.is_superuser)
    def has_object_permission(self, request, view, obj):
        print(request.auth)
        if request.user.is_superuser:
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
