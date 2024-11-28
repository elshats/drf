from rest_framework.permissions import BasePermission
from django.contrib.auth.models import AnonymousUser

from accounts.models import Accounts


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return False

        try:
            user = Accounts.objects.get(
                id=request.user.id
            )
            return user.is_staff
        except Accounts.DoesNotExist:
            return False