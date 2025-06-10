from django.http import JsonResponse
from apps.core.error_logging.logger import ErrorLogger
from rest_framework.decorators import api_view

@api_view(['GET'])
def me(request):
    try:
        return JsonResponse({
            'id': request.user.id,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        })
    except Exception as e:
        ErrorLogger.log(e, app="account", user=None)