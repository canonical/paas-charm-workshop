from django.urls import path

from .views import create_key, get_key

urlpatterns = [
    path("<str:key_id>", get_key, name="get_key"),
    path("", create_key, name="create_key"),
]
