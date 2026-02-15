"""
Auth tests: JWT obtain/refresh and 401 on protected endpoints.
"""
import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
class TestJWTAuth:
    def test_obtain_token_returns_access_and_refresh(self, api_client, user):
        url = reverse("token_obtain_pair")
        response = api_client.post(
            url,
            {"username": "testuser", "password": "testpass123"},
            format="json",
        )
        assert response.status_code == 200
        assert "access" in response.data
        assert "refresh" in response.data

    def test_obtain_token_invalid_credentials(self, api_client, user):
        url = reverse("token_obtain_pair")
        response = api_client.post(
            url,
            {"username": "testuser", "password": "wrong"},
            format="json",
        )
        assert response.status_code == 401

    def test_refresh_token_returns_new_access(self, api_client, user):
        obtain_url = reverse("token_obtain_pair")
        obtain = api_client.post(
            obtain_url,
            {"username": "testuser", "password": "testpass123"},
            format="json",
        )
        assert obtain.status_code == 200
        refresh_url = reverse("token_refresh")
        response = api_client.post(
            refresh_url,
            {"refresh": obtain.data["refresh"]},
            format="json",
        )
        assert response.status_code == 200
        assert "access" in response.data

    def test_protected_endpoint_accepts_bearer_token(self, api_client, user):
        obtain_url = reverse("token_obtain_pair")
        obtain = api_client.post(
            obtain_url,
            {"username": "testuser", "password": "testpass123"},
            format="json",
        )
        assert obtain.status_code == 200
        access = obtain.data["access"]
        url = reverse("property-list")
        response = api_client.get(
            url,
            HTTP_AUTHORIZATION=f"Bearer {access}",
        )
        assert response.status_code == 200
