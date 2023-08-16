# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DecisioningRetrieveSecretResponse"]


class DecisioningRetrieveSecretResponse(BaseModel):
    secret: Optional[str] = None
    """The 3DS Decisioning HMAC secret"""
