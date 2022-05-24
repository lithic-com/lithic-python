# File generated from our OpenAPI spec by Stainless.

from typing import Any, List, Union, Optional

from typing_extensions import Literal

from ..types import account_holder_document
from .._models import BaseModel, NoneModel, StringModel

__all__ = ["Data", "AccountHolderCreateWebhookResponse"]


class Data(BaseModel):
    hmac_token: Optional[str]
    """
    Shared secret which can optionally be used to validate the authenticity of
    incoming identity webhooks.
    """


class AccountHolderCreateWebhookResponse(BaseModel):
    data: Optional[Data]
