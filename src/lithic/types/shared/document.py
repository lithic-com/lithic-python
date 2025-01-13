# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Document", "RequiredDocumentUpload"]


class RequiredDocumentUpload(BaseModel):
    token: str
    """Globally unique identifier for the document upload."""

    accepted_entity_status_reasons: List[str]
    """
    A list of status reasons associated with a KYB account holder that have been
    satisfied by the document upload
    """

    created: datetime
    """When the document upload was created"""

    image_type: Literal["FRONT", "BACK"]
    """Type of image to upload."""

    rejected_entity_status_reasons: List[str]
    """
    A list of status reasons associated with a KYB account holder that have not been
    satisfied by the document upload
    """

    status: Literal["ACCEPTED", "REJECTED", "PENDING_UPLOAD", "UPLOADED", "PARTIAL_APPROVAL"]
    """Status of an account holder's document upload."""

    status_reasons: List[
        Literal[
            "DOCUMENT_MISSING_REQUIRED_DATA",
            "DOCUMENT_UPLOAD_TOO_BLURRY",
            "FILE_SIZE_TOO_LARGE",
            "INVALID_DOCUMENT_TYPE",
            "INVALID_DOCUMENT_UPLOAD",
            "INVALID_ENTITY",
            "DOCUMENT_EXPIRED",
            "DOCUMENT_ISSUED_GREATER_THAN_30_DAYS",
            "DOCUMENT_TYPE_NOT_SUPPORTED",
            "UNKNOWN_FAILURE_REASON",
            "UNKNOWN_ERROR",
        ]
    ]
    """Reasons for document image upload status."""

    updated: datetime
    """When the document upload was last updated"""

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
        "FINCEN_BOI_REPORT",
    ]
    """Type of documentation to be submitted for verification of an account holder"""

    entity_token: str
    """Globally unique identifier for an entity."""

    required_document_uploads: List[RequiredDocumentUpload]
    """Represents a single image of the document to upload."""
