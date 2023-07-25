# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PaymentSimulateReleaseResponse"]


class PaymentSimulateReleaseResponse(BaseModel):
    debugging_request_id: Optional[str]

    result: Optional[Literal["APPROVED", "DECLINED"]]

    transaction_event_token: Optional[str]
