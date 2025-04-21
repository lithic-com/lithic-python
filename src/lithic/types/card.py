# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .non_pci_card import NonPCICard

__all__ = ["Card"]


class Card(NonPCICard):
    cvv: Optional[str] = None
    """Three digit cvv printed on the back of the card."""

    pan: Optional[str] = None
    """Primary Account Number (PAN) (i.e.

    the card number). Customers must be PCI compliant to have PAN returned as a
    field in production. Please contact support@lithic.com for questions.
    """
