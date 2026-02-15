from rest_framework import serializers
from .models import Party


class PartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = [
            "id",
            "name",
            "party_type",
            "email",
            "phone",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]
