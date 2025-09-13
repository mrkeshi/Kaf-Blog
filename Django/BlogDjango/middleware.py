from django.http import JsonResponse
from django.conf import settings
import logging

logger = logging.getLogger(__name__)
class SecurityTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.secret_token = getattr(settings, 'PRIVATE_HEADER_KEY', None)
    def __call__(self, request):

        if request.path.startswith('/api/my-api-reverse/'):
            token = request.META.get('HTTP_NUXT_TOKEN')
            if not token or token != self.secret_token:
                return JsonResponse({'error': 'Unauthorized'}, status=401)
        return self.get_response(request)

