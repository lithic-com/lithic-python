# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ..types import account_holder_document
from .._models import BaseModel

__all__ = ["AccountHolderListDocumentsResponse"]


class AccountHolderListDocumentsResponse(BaseModel):
    data: Optional[List[account_holder_document.AccountHolderDocument]]
