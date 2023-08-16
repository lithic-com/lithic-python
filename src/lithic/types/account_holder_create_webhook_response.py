# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["AccountHolderCreateWebhookResponse", "Data"]


class Data(BaseModel):
    hmac_token: Optional[str] = None
    """
    Shared secret which can optionally be used to validate the authenticity of
    incoming identity webhooks.
    """


class AccountHolderCreateWebhookResponse(BaseModel):
    data: Optional[Data] = None
