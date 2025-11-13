# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentReturnResponse"]


class PaymentReturnResponse(BaseModel):
    result: Literal["APPROVED", "DECLINED"]
    """Transaction result"""

    transaction_group_uuid: str
    """Globally unique identifier for the transaction group"""

    transaction_uuid: str
    """Globally unique identifier for the transaction"""
