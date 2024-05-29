# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentSimulateReceiptResponse"]


class PaymentSimulateReceiptResponse(BaseModel):
    debugging_request_id: str
    """Debugging Request Id"""

    result: Literal["APPROVED", "DECLINED"]
    """Request Result"""

    transaction_event_token: str
    """Transaction Event Token"""
