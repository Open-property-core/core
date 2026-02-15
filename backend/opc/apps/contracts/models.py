from django.db import models

from opc.apps.parties.models import Party
from opc.apps.properties.models import Unit


class Contract(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        ACTIVE = "active", "Active"
        TERMINATED = "terminated", "Terminated"

    unit = models.ForeignKey(
        Unit,
        on_delete=models.CASCADE,
        related_name="contracts",
    )
    party = models.ForeignKey(
        Party,
        on_delete=models.CASCADE,
        related_name="contracts",
    )
    start_date = models.DateField()
    end_date = models.DateField()
    monthly_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.unit} — {self.party} ({self.status})"
