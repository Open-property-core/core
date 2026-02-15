from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .tasks import hello_celery


@api_view(["POST"])
@permission_classes([AllowAny])
def trigger_hello_celery(request):
    """Trigger the sample Celery task; returns task id for verification."""
    result = hello_celery.delay()
    return Response(
        {"task_id": result.id, "status": "sent"},
        status=status.HTTP_202_ACCEPTED,
    )
