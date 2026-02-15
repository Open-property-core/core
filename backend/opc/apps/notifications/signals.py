"""
Connect notification services to model events.
"""
from django.db.models.signals import post_save
from django.dispatch import receiver

from opc.apps.contracts.models import Contract
from opc.apps.notifications.services import send_contract_created_email


@receiver(post_save, sender=Contract)
def on_contract_created(sender, instance, created, **kwargs):
    if created:
        send_contract_created_email(instance)
