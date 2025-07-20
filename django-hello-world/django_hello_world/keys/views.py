import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import SecretKey


# Create your views here.
@csrf_exempt  # Disable CSRF for simplicity; consider using CSRF tokens in production
@require_http_methods(["GET"])
def get_key(request, key_id):
    try:
        key_value = SecretKey.objects.get(id=key_id)
        return JsonResponse({"key_id": key_value.id, "value": key_value.value})
    except SecretKey.DoesNotExist:
        return JsonResponse({"error": "Key not found"}, status=404)


@csrf_exempt  # Disable CSRF for simplicity
@require_http_methods(["POST"])
def create_key(request):
    body = json.loads(request.body)
    value = body.get("value")
    key_value = SecretKey.objects.create(value=value)
    return JsonResponse({"key_id": key_value.id}, status=201)
