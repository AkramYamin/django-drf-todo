from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
        Custom permission decorator to enable only
        the owner of a task, otherwise no access
    """

    def has_object_permission(self, request, view, obj):
        """
            Read permissions and check if the requested
            object can be returned
            :param self: the IsOwnerOrReadOnly class
            :param request: the request made by the user
            :param view: the impacted view of the request
            :param obj: the requested object
        """

        return obj.owner == request.user
