"""
Notification services. Phase 2: email notifications for contract and payment events.
"""
import logging

from django.core.mail import send_mail

logger = logging.getLogger(__name__)


def send_contract_created_email(contract) -> bool:
    """
    Send email notification when a contract is created.
    Sends to the party's email if available.
    """
    party = contract.party
    if not party.email:
        logger.debug("Contract %s: party has no email, skipping notification", contract.id)
        return False

    subject = f"Contract created: {contract.unit} — {contract.party}"
    message = (
        f"A new contract has been created.\n\n"
        f"Unit: {contract.unit}\n"
        f"Party: {contract.party}\n"
        f"Start: {contract.start_date}\n"
        f"End: {contract.end_date}\n"
        f"Monthly amount: {contract.monthly_amount}\n"
    )
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=None,  # uses DEFAULT_FROM_EMAIL
            recipient_list=[party.email],
            fail_silently=True,
        )
        return True
    except Exception as e:
        logger.warning("Failed to send contract notification email: %s", e)
        return False
