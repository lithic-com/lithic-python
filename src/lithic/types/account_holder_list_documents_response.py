# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .shared.document import Document

__all__ = ["AccountHolderListDocumentsResponse"]


class AccountHolderListDocumentsResponse(BaseModel):
    data: Optional[List[Document]] = None
