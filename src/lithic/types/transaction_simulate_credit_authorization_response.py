# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["TransactionSimulateCreditAuthorizationResponse"]


class TransactionSimulateCreditAuthorizationResponse(BaseModel):
    token: Optional[str] = None
    """A unique token to reference this transaction."""

    debugging_request_id: Optional[str] = None
    """Debugging request ID to share with Lithic Support team."""
