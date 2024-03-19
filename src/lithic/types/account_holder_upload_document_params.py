# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountHolderUploadDocumentParams"]


class AccountHolderUploadDocumentParams(TypedDict, total=False):
    document_type: Required[Literal["commercial_license", "drivers_license", "passport", "passport_card", "visa"]]
    """Type of the document to upload."""
