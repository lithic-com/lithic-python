# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .tokenization import Tokenization

__all__ = ["TokenizationSimulateResponse"]


class TokenizationSimulateResponse(BaseModel):
    data: Optional[List[Tokenization]] = None
