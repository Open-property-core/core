from rest_framework import serializers
from .models import Contract
from opc.apps.parties.serializers import PartySerializer
from opc.apps.properties.serializers import UnitSerializer


class ContractSerializer(serializers.ModelSerializer):
    unit_detail = UnitSerializer(source="unit", read_only=True)
    party_detail = PartySerializer(source="party", read_only=True)

    class Meta:
        model = Contract
        fields = [
            "id",
            "unit",
            "unit_detail",
            "party",
            "party_detail",
            "start_date",
            "end_date",
            "monthly_amount",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class ContractListSerializer(serializers.ModelSerializer):
    """Light serializer for list (IDs only for FK)."""

    class Meta:
        model = Contract
        fields = [
            "id",
            "unit",
            "party",
            "start_date",
            "end_date",
            "monthly_amount",
            "status",
            "created_at",
            "updated_at",
        ]
