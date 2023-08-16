# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["TokenizationDecisioningRotateSecretResponse"]


class TokenizationDecisioningRotateSecretResponse(BaseModel):
    secret: Optional[str] = None
    """The new Tokenization Decisioning HMAC secret"""
