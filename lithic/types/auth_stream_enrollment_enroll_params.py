# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import Optional, Union, List
from typing_extensions import Literal, TypedDict, Required
from ..types import shared_params

__all__ = ["AuthStreamEnrollmentEnrollParams"]


class AuthStreamEnrollmentEnrollParams(TypedDict, total=False):
    webhook_url: str
    """A user-specified url to receive and respond to ASA request."""
