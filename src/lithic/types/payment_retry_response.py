# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .balance import Balance
from .payment import Payment

__all__ = ["PaymentRetryResponse"]


class PaymentRetryResponse(Payment):
    balance: Optional[Balance] = None
    """Balance"""
