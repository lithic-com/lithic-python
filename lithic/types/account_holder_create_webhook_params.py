# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import Optional, Union, List
from typing_extensions import Literal, TypedDict, Required
from ..types import shared_params

__all__ = ["AccountHolderCreateWebhookParams"]


class AccountHolderCreateWebhookParams(TypedDict, total=False):
    url: Required[str]
    """URL to receive webhook requests. Must be a valid HTTPS address."""
