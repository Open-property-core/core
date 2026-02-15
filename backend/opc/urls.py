from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/v1/token/",
        TokenObtainPairView.as_view(permission_classes=[AllowAny]),
        name="token_obtain_pair",
    ),
    path(
        "api/v1/token/refresh/",
        TokenRefreshView.as_view(permission_classes=[AllowAny]),
        name="token_refresh",
    ),
    path("api/v1/", include("opc.apps.core.urls")),
    path("api/v1/", include("opc.apps.properties.urls")),
    path("api/v1/", include("opc.apps.parties.urls")),
    path("api/v1/", include("opc.apps.contracts.urls")),
    path("api/v1/", include("opc.apps.billing.urls")),
    path("api/schema/", include("drf_spectacular.urls")),
]
