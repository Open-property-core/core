from rest_framework import serializers
from .models import Property, Unit


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = [
            "id",
            "property",
            "name",
            "area",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class PropertySerializer(serializers.ModelSerializer):
    units = UnitSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = [
            "id",
            "name",
            "address",
            "property_type",
            "status",
            "units",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class PropertyListSerializer(serializers.ModelSerializer):
    """Light serializer for list views (no nested units)."""

    class Meta:
        model = Property
        fields = [
            "id",
            "name",
            "address",
            "property_type",
            "status",
            "created_at",
            "updated_at",
        ]
