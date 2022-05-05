# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Any
from typing_extensions import Literal
from .._models import StringModel, NoneModel, BaseModel
from ..types import card


__all__ = ["TransactionSimulateVoidResponse"]


class TransactionSimulateVoidResponse(BaseModel):
    debugging_request_id: Optional[str]
    """Debugging request ID to share with Lithic Support team."""
