from rest_framework import viewsets
from .models import Contract
from .serializers import ContractSerializer, ContractListSerializer


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.select_related("unit", "party", "unit__property").all()
    serializer_class = ContractSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ContractListSerializer
        return ContractSerializer
