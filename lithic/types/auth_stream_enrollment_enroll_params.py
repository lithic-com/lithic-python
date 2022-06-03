# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AuthStreamEnrollmentEnrollParams"]


class AuthStreamEnrollmentEnrollParams(TypedDict, total=False):
    webhook_url: str
    """A user-specified url to receive and respond to ASA request."""
