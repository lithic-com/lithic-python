# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["AuthStreamSecret"]


class AuthStreamSecret(BaseModel):
    secret: Optional[str]
    """The shared HMAC ASA secret"""
