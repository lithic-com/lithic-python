# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Any
from typing_extensions import Literal
from .._models import StringModel, NoneModel, BaseModel
from ..types import account_holder_document


__all__ = ["AccountHolderListDocumentsResponse"]


class AccountHolderListDocumentsResponse(BaseModel):
    data: Optional[List[account_holder_document.AccountHolderDocument]]
