from django.db import models


class Property(models.Model):
    class PropertyType(models.TextChoices):
        RESIDENTIAL = "residential", "Residential"
        COMMERCIAL = "commercial", "Commercial"
        MIXED = "mixed", "Mixed"

    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    property_type = models.CharField(
        max_length=20,
        choices=PropertyType.choices,
        default=PropertyType.RESIDENTIAL,
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Properties"
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class Unit(models.Model):
    class Status(models.TextChoices):
        AVAILABLE = "available", "Available"
        OCCUPIED = "occupied", "Occupied"
        MAINTENANCE = "maintenance", "Maintenance"

    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="units",
    )
    name = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.AVAILABLE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["property", "name"]
        unique_together = [["property", "name"]]

    def __str__(self):
        return f"{self.name} ({self.property.name})"
