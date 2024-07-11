# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .tokenization import Tokenization

__all__ = ["TokenizationUpdateDigitalCardArtResponse"]


class TokenizationUpdateDigitalCardArtResponse(BaseModel):
    data: Optional[Tokenization] = None
