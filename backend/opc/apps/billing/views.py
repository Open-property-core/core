from rest_framework import viewsets
from .models import Invoice, Payment
from .serializers import (
    InvoiceSerializer,
    InvoiceListSerializer,
    PaymentSerializer,
)


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.select_related("contract").prefetch_related("payments").all()
    serializer_class = InvoiceSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return InvoiceListSerializer
        return InvoiceSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.select_related("invoice").all()
    serializer_class = PaymentSerializer
