"""
Shared fixtures for API tests.
"""
import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient

User = get_user_model()


@pytest.fixture
def api_client():
    """DRF API client (unauthenticated)."""
    return APIClient()


@pytest.fixture
def user(db):
    """A regular user for auth tests."""
    return User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="testpass123",
    )


@pytest.fixture
def authenticated_client(api_client, user):
    """API client authenticated as user."""
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def property_payload():
    return {
        "name": "Test Building",
        "address": "123 Test St",
        "property_type": "residential",
        "status": "active",
    }


@pytest.fixture
def party_payload():
    return {
        "name": "Test Tenant",
        "party_type": "tenant",
        "email": "tenant@test.example",
        "phone": "+79001234567",
    }
