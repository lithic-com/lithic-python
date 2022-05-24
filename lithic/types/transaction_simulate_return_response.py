# File generated from our OpenAPI spec by Stainless.

from typing import Any, List, Union, Optional

from typing_extensions import Literal

from ..types import card
from .._models import BaseModel, NoneModel, StringModel

__all__ = ["TransactionSimulateReturnResponse"]


class TransactionSimulateReturnResponse(BaseModel):
    debugging_request_id: Optional[str]
    """Debugging request ID to share with Lithic Support team."""

    token: Optional[str]
    """A unique token to reference this transaction."""
