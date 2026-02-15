"""
Application layer (DDD): use cases for contracts.
Views call these instead of putting business logic in ViewSets.
"""
from opc.apps.contracts.models import Contract


def get_contract_list(*, queryset=None):
    """Return contracts for list/read use cases. Optional base queryset for filtering."""
    if queryset is None:
        queryset = Contract.objects.select_related("unit", "party", "unit__property")
    return queryset.all()
