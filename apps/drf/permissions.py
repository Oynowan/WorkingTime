from rest_framework import permissions


class IsOwnerSupervisorOrReadOnlyWorkingTime(permissions.BasePermission):
    """
    Custom permission to only allow owners or supervisors to edit object.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.users_time.user == request.user or request.user.userprofile.supervisor


class IsOwnerSupervisorOrReadOnlyUserProfile(permissions.BasePermission):
    """
    Custom permission to only allow owners or supervisors to edit object.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.user == request.user or request.user.userprofile.supervisor


