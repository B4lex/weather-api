from functools import wraps

from django.conf import settings
from rest_framework.exceptions import PermissionDenied


def enforce_anti_spam_token_check(method):
    @wraps(method)
    def wrapper(request, *args, **kwargs):
        if request.headers.get("x-token") != settings.ANTI_SPAM_TOKEN:
            raise PermissionDenied("'X-Token' header is missing or invalid.")
        return method(request, *args, **kwargs)

    return wrapper
