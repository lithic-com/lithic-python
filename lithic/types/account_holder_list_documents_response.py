# File generated from our OpenAPI spec by Stainless.

from typing import Any, List, Union, Optional

from typing_extensions import Literal

from ..types import account_holder_document
from .._models import BaseModel, NoneModel, StringModel

__all__ = ["AccountHolderListDocumentsResponse"]


class AccountHolderListDocumentsResponse(BaseModel):
    data: Optional[List[account_holder_document.AccountHolderDocument]]
