from rest_framework import viewsets
from .models import Property, Unit
from .serializers import PropertySerializer, PropertyListSerializer, UnitSerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.prefetch_related("units").all()
    serializer_class = PropertySerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PropertyListSerializer
        return PropertySerializer


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.select_related("property").all()
    serializer_class = UnitSerializer
