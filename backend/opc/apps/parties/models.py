from django.db import models


class Party(models.Model):
    class PartyType(models.TextChoices):
        TENANT = "tenant", "Tenant"
        LANDLORD = "landlord", "Landlord"
        MANAGER = "manager", "Manager"

    name = models.CharField(max_length=255)
    party_type = models.CharField(
        max_length=20,
        choices=PartyType.choices,
        default=PartyType.TENANT,
    )
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Parties"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
