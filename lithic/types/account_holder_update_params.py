# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AccountHolderUpdateParams"]


class AccountHolderUpdateParams(TypedDict, total=False):
    email: str
    """Account holder's email address.

    The primary purpose of this field is for cardholder identification and
    verification during the digital wallet tokenization process.
    """

    phone_number: str
    """Account holder's phone number, entered in E.164 format.

    The primary purpose of this field is for cardholder identification and
    verification during the digital wallet tokenization process.
    """
