from rest_framework import serializers
from .models import Invoice, Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id",
            "invoice",
            "amount",
            "paid_at",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class InvoiceSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = [
            "id",
            "contract",
            "amount",
            "due_date",
            "status",
            "payments",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class InvoiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = [
            "id",
            "contract",
            "amount",
            "due_date",
            "status",
            "created_at",
            "updated_at",
        ]
