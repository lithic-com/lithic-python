# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..types import payment
from ..types.balance import Balance

__all__ = ["PaymentCreateResponse"]


class PaymentCreateResponse(payment.Payment):
    balance: Optional[Balance]
    """Balance of a Financial Account"""
