from django.core.exceptions import PermissionDenied

class AdminRequiredMixin:
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            raise PermissionDenied("You don't have permission to access this page.")
        return super().dispatch(request, *args, **kwargs)
