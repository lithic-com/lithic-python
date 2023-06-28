# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["TransactionSimulateAuthorizationAdviceResponse"]


class TransactionSimulateAuthorizationAdviceResponse(BaseModel):
    token: Optional[str]
    """A unique token to reference this transaction."""

    debugging_request_id: Optional[str]
    """Debugging request ID to share with Lithic Support team."""
