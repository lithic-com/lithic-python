# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentSimulateReturnResponse"]


class PaymentSimulateReturnResponse(BaseModel):
    debugging_request_id: Optional[str] = None

    result: Optional[Literal["APPROVED", "DECLINED"]] = None

    transaction_event_token: Optional[str] = None
