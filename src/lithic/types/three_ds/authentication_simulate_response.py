# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["AuthenticationSimulateResponse"]


class AuthenticationSimulateResponse(BaseModel):
    token: Optional[str] = None
    """
    A unique token to reference this transaction with later calls to void or clear
    the authorization.
    """

    debugging_request_id: Optional[str] = None
    """Debugging request ID to share with Lithic Support team."""
