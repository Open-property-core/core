from django.contrib import admin
from .models import Property, Unit


class UnitInline(admin.TabularInline):
    model = Unit
    extra = 0


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("name", "property_type", "status", "created_at")
    list_filter = ("property_type", "status")
    search_fields = ("name", "address")
    inlines = [UnitInline]


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("name", "property", "area", "status", "created_at")
    list_filter = ("status", "property")
    search_fields = ("name",)
