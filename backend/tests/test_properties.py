"""
API tests for properties and units.
"""
import pytest
from django.urls import reverse
from opc.apps.properties.models import Property, Unit


@pytest.mark.django_db
class TestPropertyAPI:
    def test_list_requires_auth(self, api_client):
        url = reverse("property-list")
        response = api_client.get(url)
        assert response.status_code == 401

    def test_list_empty(self, authenticated_client):
        url = reverse("property-list")
        response = authenticated_client.get(url)
        assert response.status_code == 200
        assert response.data["results"] == []

    def test_create_property(self, authenticated_client, property_payload):
        url = reverse("property-list")
        response = authenticated_client.post(url, property_payload, format="json")
        assert response.status_code == 201
        assert response.data["name"] == property_payload["name"]
        assert response.data["property_type"] == property_payload["property_type"]
        assert "id" in response.data
        assert Property.objects.filter(name=property_payload["name"]).exists()

    def test_retrieve_property(self, authenticated_client, property_payload):
        prop = Property.objects.create(**property_payload)
        url = reverse("property-detail", kwargs={"pk": prop.pk})
        response = authenticated_client.get(url)
        assert response.status_code == 200
        assert response.data["id"] == prop.pk
        assert response.data["name"] == prop.name

    def test_update_property(self, authenticated_client, property_payload):
        prop = Property.objects.create(**property_payload)
        url = reverse("property-detail", kwargs={"pk": prop.pk})
        response = authenticated_client.patch(
            url, {"name": "Updated Name"}, format="json"
        )
        assert response.status_code == 200
        prop.refresh_from_db()
        assert prop.name == "Updated Name"

    def test_delete_property(self, authenticated_client, property_payload):
        prop = Property.objects.create(**property_payload)
        url = reverse("property-detail", kwargs={"pk": prop.pk})
        response = authenticated_client.delete(url)
        assert response.status_code == 204
        assert not Property.objects.filter(pk=prop.pk).exists()


@pytest.mark.django_db
class TestUnitAPI:
    def test_list_requires_auth(self, api_client):
        url = reverse("unit-list")
        response = api_client.get(url)
        assert response.status_code == 401

    def test_list_empty(self, authenticated_client):
        url = reverse("unit-list")
        response = authenticated_client.get(url)
        assert response.status_code == 200
        assert response.data["results"] == []

    def test_create_unit(self, authenticated_client, property_payload):
        prop = Property.objects.create(**property_payload)
        unit_payload = {
            "property": prop.pk,
            "name": "Unit 101",
            "area": "45.50",
            "status": "available",
        }
        url = reverse("unit-list")
        response = authenticated_client.post(url, unit_payload, format="json")
        assert response.status_code == 201
        assert response.data["name"] == unit_payload["name"]
        assert response.data["property"] == prop.pk
        assert Unit.objects.filter(property=prop, name="Unit 101").exists()

    def test_retrieve_unit(self, authenticated_client, property_payload):
        prop = Property.objects.create(**property_payload)
        unit = Unit.objects.create(property=prop, name="Unit 1", status="available")
        url = reverse("unit-detail", kwargs={"pk": unit.pk})
        response = authenticated_client.get(url)
        assert response.status_code == 200
        assert response.data["id"] == unit.pk
        assert response.data["name"] == unit.name
