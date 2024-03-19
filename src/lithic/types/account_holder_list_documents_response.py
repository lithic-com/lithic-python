# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .account_holder_document import AccountHolderDocument

__all__ = ["AccountHolderListDocumentsResponse"]


class AccountHolderListDocumentsResponse(BaseModel):
    data: Optional[List[AccountHolderDocument]] = None
