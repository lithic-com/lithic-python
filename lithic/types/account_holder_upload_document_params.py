# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List, Union, Optional

from typing_extensions import Literal, Required, TypedDict

from ..types import shared_params

__all__ = ["AccountHolderUploadDocumentParams"]


class AccountHolderUploadDocumentParams(TypedDict, total=False):
    document_type: Required[Literal["COMMERCIAL_LICENCE", "DRIVERS_LICENSE", "PASSPORT", "PASSPORT_CARD", "VISA"]]
    """Type of the document to upload."""
