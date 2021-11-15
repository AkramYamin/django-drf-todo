from rest_framework import permissions


class IsAuthenticatedAndOwner(permissions.BasePermission):
    """
        Custom permission decorator to enable only authenticated and user
        and the owner of a task, otherwise no access
    """

    def has_permission(self, request, view):
        """
            check if the user authenticated to access this API(view) at all
        :param request: request object
        :param view: view name
        :return: True if the user authenticated
        """
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        """
            Read permissions and check if the requested
            object can be returned
            :param self: the IsAuthenticatedAndOwner class
            :param request: the request made by the user
            :param view: the impacted view of the request
            :param obj: the requested object
        """

        return obj.owner == request.user
