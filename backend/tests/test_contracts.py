"""
API tests for contracts.
"""
from decimal import Decimal

import pytest
from django.urls import reverse
from opc.apps.contracts.models import Contract
from opc.apps.parties.models import Party
from opc.apps.properties.models import Property, Unit


@pytest.fixture
def contract_data(property_payload, party_payload):
    """Create property, unit, party for contract tests."""
    prop = Property.objects.create(**property_payload)
    unit = Unit.objects.create(
        property=prop, name="Unit 1", status="available"
    )
    party = Party.objects.create(**party_payload)
    return {
        "unit": unit,
        "party": party,
        "payload": {
            "unit": unit.pk,
            "party": party.pk,
            "start_date": "2025-01-01",
            "end_date": "2025-12-31",
            "monthly_amount": "50000.00",
            "status": "draft",
        },
    }


@pytest.mark.django_db
class TestContractAPI:
    def test_list_requires_auth(self, api_client):
        url = reverse("contract-list")
        response = api_client.get(url)
        assert response.status_code == 401

    def test_list_empty(self, authenticated_client):
        url = reverse("contract-list")
        response = authenticated_client.get(url)
        assert response.status_code == 200
        assert response.data["results"] == []

    def test_create_contract(self, authenticated_client, contract_data):
        url = reverse("contract-list")
        response = authenticated_client.post(
            url, contract_data["payload"], format="json"
        )
        assert response.status_code == 201
        assert response.data["unit"] == contract_data["unit"].pk
        assert response.data["party"] == contract_data["party"].pk
        assert response.data["status"] == "draft"
        assert Decimal(response.data["monthly_amount"]) == Decimal(
            "50000.00"
        )
        assert Contract.objects.filter(
            unit=contract_data["unit"], party=contract_data["party"]
        ).exists()

    def test_retrieve_contract(self, authenticated_client, contract_data):
        contract = Contract.objects.create(
            unit=contract_data["unit"],
            party=contract_data["party"],
            start_date=contract_data["payload"]["start_date"],
            end_date=contract_data["payload"]["end_date"],
            monthly_amount=Decimal(
                contract_data["payload"]["monthly_amount"]
            ),
            status="draft",
        )
        url = reverse("contract-detail", kwargs={"pk": contract.pk})
        response = authenticated_client.get(url)
        assert response.status_code == 200
        assert response.data["id"] == contract.pk
        assert response.data["unit_detail"]["name"] == contract_data["unit"].name
        assert response.data["party_detail"]["name"] == contract_data["party"].name

    def test_update_contract_status(self, authenticated_client, contract_data):
        contract = Contract.objects.create(
            unit=contract_data["unit"],
            party=contract_data["party"],
            start_date=contract_data["payload"]["start_date"],
            end_date=contract_data["payload"]["end_date"],
            monthly_amount=Decimal(
                contract_data["payload"]["monthly_amount"]
            ),
            status="draft",
        )
        url = reverse("contract-detail", kwargs={"pk": contract.pk})
        response = authenticated_client.patch(
            url, {"status": "active"}, format="json"
        )
        assert response.status_code == 200
        contract.refresh_from_db()
        assert contract.status == "active"
