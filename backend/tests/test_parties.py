"""
API tests for parties.
"""
import pytest
from django.urls import reverse
from opc.apps.parties.models import Party


@pytest.mark.django_db
class TestPartyAPI:
    def test_list_requires_auth(self, api_client):
        url = reverse("party-list")
        response = api_client.get(url)
        assert response.status_code == 401

    def test_list_empty(self, authenticated_client):
        url = reverse("party-list")
        response = authenticated_client.get(url)
        assert response.status_code == 200
        assert response.data["results"] == []

    def test_create_party(self, authenticated_client, party_payload):
        url = reverse("party-list")
        response = authenticated_client.post(url, party_payload, format="json")
        assert response.status_code == 201
        assert response.data["name"] == party_payload["name"]
        assert response.data["party_type"] == party_payload["party_type"]
        assert "id" in response.data
        assert Party.objects.filter(name=party_payload["name"]).exists()

    def test_retrieve_party(self, authenticated_client, party_payload):
        party = Party.objects.create(**party_payload)
        url = reverse("party-detail", kwargs={"pk": party.pk})
        response = authenticated_client.get(url)
        assert response.status_code == 200
        assert response.data["id"] == party.pk
        assert response.data["name"] == party.name

    def test_update_party(self, authenticated_client, party_payload):
        party = Party.objects.create(**party_payload)
        url = reverse("party-detail", kwargs={"pk": party.pk})
        response = authenticated_client.patch(
            url, {"name": "Updated Party"}, format="json"
        )
        assert response.status_code == 200
        party.refresh_from_db()
        assert party.name == "Updated Party"

    def test_delete_party(self, authenticated_client, party_payload):
        party = Party.objects.create(**party_payload)
        url = reverse("party-detail", kwargs={"pk": party.pk})
        response = authenticated_client.delete(url)
        assert response.status_code == 204
        assert not Party.objects.filter(pk=party.pk).exists()
