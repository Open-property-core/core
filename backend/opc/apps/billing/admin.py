from django.contrib import admin
from .models import Invoice, Payment


class PaymentInline(admin.TabularInline):
    model = Payment
    extra = 0


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ("id", "contract", "amount", "due_date", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("contract__id",)
    raw_id_fields = ("contract",)
    inlines = [PaymentInline]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "invoice", "amount", "paid_at", "status", "created_at")
    list_filter = ("status",)
    raw_id_fields = ("invoice",)
