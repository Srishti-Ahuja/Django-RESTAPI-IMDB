from rest_framework.exceptions import ValidationError
from rest_framework.permissions import BasePermission

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method=="GET":
            return True
        elif obj.reviewer != request.user:
            raise ValidationError("Only reviewer can edit their reviews", 400)
        return True