from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PartyViewSet

router = DefaultRouter()
router.register(r"parties", PartyViewSet, basename="party")

app_name = "parties"
urlpatterns = [
    path("", include(router.urls)),
]
