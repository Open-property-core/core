"""
Tests for core app (e.g. Celery trigger view).
"""
import pytest
from django.urls import reverse
from opc.apps.core.tasks import hello_celery


@pytest.mark.django_db
class TestTriggerHelloCelery:
    def test_trigger_returns_202_and_task_id(self, api_client):
        url = reverse("core:trigger_hello_celery")
        response = api_client.post(url, {}, format="json")
        assert response.status_code == 202
        assert "task_id" in response.data
        assert response.data.get("status") == "sent"


class TestHelloCeleryTask:
    def test_hello_celery_returns_ok(self):
        # CELERY_TASK_ALWAYS_EAGER = True in test settings
        result = hello_celery.delay()
        assert result.get() == "ok"
