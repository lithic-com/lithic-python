# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["TransactionSimulateReturnReversalResponse"]


class TransactionSimulateReturnReversalResponse(BaseModel):
    debugging_request_id: Optional[str] = None
    """Debugging request ID to share with Lithic Support team."""
