# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["TokenizationSecret"]


class TokenizationSecret(BaseModel):
    secret: Optional[str]
    """The Tokenization Decisioning HMAC secret"""
