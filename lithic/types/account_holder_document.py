# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RequiredDocumentUploads", "AccountHolderDocument"]


class RequiredDocumentUploads(BaseModel):
    image_type: Optional[Literal["back", "front"]]
    """Type of image to upload."""

    status: Optional[Literal["COMPLETED", "FAILED", "PENDING", "UPLOADED"]]
    """Status of document image upload."""

    status_reasons: Optional[
        List[
            Literal[
                "BACK_IMAGE_BLURRY",
                "FILE_SIZE_TOO_LARGE",
                "FRONT_IMAGE_BLURRY",
                "FRONT_IMAGE_GLARE",
                "INVALID_FILE_TYPE",
                "UNKNOWN_ERROR",
            ]
        ]
    ]

    upload_url: Optional[str]
    """URL to upload document image to.

    Note that the upload URLs expire after 7 days. If an upload URL expires, you can
    refresh the URLs by retrieving the document upload from
    `GET /account_holders/{account_holder_token}/documents`.
    """


class AccountHolderDocument(BaseModel):
    account_token: Optional[str]
    """Globally unique identifier for the account."""

    document_type: Optional[Literal["commercial_license", "drivers_license", "passport", "passport_card", "visa"]]
    """Type of documentation to be submitted for verification."""

    required_document_uploads: Optional[List[RequiredDocumentUploads]]

    token: Optional[str]
    """Globally unique identifier for the document."""
