from functools import wraps
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
# from .models import ErrorLogger
from apps.core.error_logging.logger import ErrorLogger

def catch_api_errors(app_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request = None
            # Try to extract request (function-based vs class-based)
            if args:
                if hasattr(args[0], 'META'):
                    request = args[0]  # function-based view
                elif len(args) > 1 and hasattr(args[1], 'META'):
                    request = args[1]  # class-based view: self, request
            try:
                return func(*args, **kwargs)
            except ObjectDoesNotExist as e:
                if request:
                      # or your actual import
                    ErrorLogger.log(e, app=app_name, user=request.user if getattr(request, 'user', None) and request.user.is_authenticated else None)
                return JsonResponse({"error": "Not found"}, status=404)
            except Exception as e:
                if request:
                    ErrorLogger.log(e, app=app_name, user=request.user if getattr(request, 'user', None) and request.user.is_authenticated else None)
                return JsonResponse({"error": "An unexpected error occurred"}, status=500)
        return wrapper
    return decorator


def catch_admin_errors(app_name):
    def decorator(func):
        @wraps(func)
        def wrapper(modeladmin, request, *args, **kwargs):
            try:
                return func(modeladmin, request, *args, **kwargs)
            except Exception as e:
                user = request.user if request.user.is_authenticated else None
                ErrorLogger.log(e, app=app_name, user=user)
                raise
        return wrapper
    return decorator

def catch_errors(app_name):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                ErrorLogger.log(e, app=app_name, user=None)
                raise
        return wrapper
    return decorator
