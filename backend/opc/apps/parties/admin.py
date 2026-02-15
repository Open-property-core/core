from django.contrib import admin
from .models import Party


@admin.register(Party)
class PartyAdmin(admin.ModelAdmin):
    list_display = ("name", "party_type", "email", "phone", "created_at")
    list_filter = ("party_type",)
    search_fields = ("name", "email")
