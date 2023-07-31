# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DescisioningRetrieveSecretResponse"]


class DescisioningRetrieveSecretResponse(BaseModel):
    secret: Optional[str]
    """The 3DS Decisioning HMAC secret"""
