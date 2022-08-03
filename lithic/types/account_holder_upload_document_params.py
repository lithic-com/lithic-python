# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountHolderUploadDocumentParams"]


class AccountHolderUploadDocumentParams(TypedDict, total=False):
    document_type: Required[Literal["COMMERCIAL_LICENSE", "DRIVERS_LICENSE", "PASSPORT", "PASSPORT_CARD", "VISA"]]
    """Type of the document to upload."""
