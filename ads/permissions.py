from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    A custom permission class.
    Allows access only to an object's owner.
    """
    message = 'You are not the owner of the ad'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author:
            return True
        else:
            return False
