# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Any
from typing_extensions import Literal
from .._models import StringModel, NoneModel, BaseModel
from ..types import account_holder_document


__all__ = ["Data", "AccountHolderCreateWebhookResponse"]


class Data(BaseModel):
    hmac_token: Optional[str]
    """Shared secret which can optionally be used to validate the authenticity of incoming identity webhooks."""


class AccountHolderCreateWebhookResponse(BaseModel):
    data: Optional[Data]
