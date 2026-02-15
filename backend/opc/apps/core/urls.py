from django.urls import path
from .views import trigger_hello_celery

app_name = "core"
urlpatterns = [
    path("trigger-hello-celery/", trigger_hello_celery, name="trigger_hello_celery"),
]
