from django.contrib import admin
from .models import Contract


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("unit", "party", "start_date", "end_date", "monthly_amount", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("unit__name", "party__name")
    raw_id_fields = ("unit", "party")
