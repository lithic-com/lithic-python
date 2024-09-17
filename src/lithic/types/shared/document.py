# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Document", "RequiredDocumentUpload"]


class RequiredDocumentUpload(BaseModel):
    token: str
    """Globally unique identifier for the document upload."""

    image_type: Literal["FRONT", "BACK"]
    """Type of image to upload."""

    status: Literal["ACCEPTED", "REJECTED", "PENDING_UPLOAD", "UPLOADED"]
    """Status of document image upload."""

    status_reasons: List[
        Literal[
            "DOCUMENT_MISSING_REQUIRED_DATA",
            "DOCUMENT_UPLOAD_TOO_BLURRY",
            "FILE_SIZE_TOO_LARGE",
            "INVALID_DOCUMENT_TYPE",
            "INVALID_DOCUMENT_UPLOAD",
            "UNKNOWN_ERROR",
        ]
    ]
    """Reasons for document image upload status."""

    upload_url: str
    """URL to upload document image to.

    Note that the upload URLs expire after 7 days. If an upload URL expires, you can
    refresh the URLs by retrieving the document upload from
    `GET /account_holders/{account_holder_token}/documents`.
    """


class Document(BaseModel):
    token: str
    """Globally unique identifier for the document."""

    account_holder_token: str
    """Globally unique identifier for the account holder."""

    document_type: Literal[
        "DRIVERS_LICENSE",
        "PASSPORT",
        "PASSPORT_CARD",
        "EIN_LETTER",
        "TAX_RETURN",
        "OPERATING_AGREEMENT",
        "CERTIFICATE_OF_FORMATION",
        "CERTIFICATE_OF_GOOD_STANDING",
        "ARTICLES_OF_INCORPORATION",
        "ARTICLES_OF_ORGANIZATION",
        "BYLAWS",
        "GOVERNMENT_BUSINESS_LICENSE",
        "PARTNERSHIP_AGREEMENT",
        "SS4_FORM",
        "BANK_STATEMENT",
        "UTILITY_BILL_STATEMENT",
        "SSN_CARD",
        "ITIN_LETTER",
    ]
    """Type of documentation to be submitted for verification."""

    entity_token: str
    """Globally unique identifier for an entity."""

    required_document_uploads: List[RequiredDocumentUpload]
    """Represents a single image of the document to upload."""
