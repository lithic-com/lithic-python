# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountHolderDocumentUpdatedWebhookEvent", "RequiredDocumentUpload"]


class RequiredDocumentUpload(BaseModel):
    """A document upload that belongs to the overall account holder document"""

    token: Optional[str] = None
    """The token of the document upload"""

    accepted_entity_status_reasons: Optional[List[str]] = None

    created: Optional[datetime] = None
    """When the document upload was created"""

    image_type: Optional[Literal["FRONT", "BACK"]] = None
    """The type of image that was uploaded"""

    rejected_entity_status_reasons: Optional[List[str]] = None

    status: Optional[Literal["ACCEPTED", "REJECTED", "PENDING_UPLOAD", "UPLOADED", "PARTIAL_APPROVAL"]] = None
    """The status of the document upload"""

    status_reasons: Optional[List[str]] = None

    updated: Optional[datetime] = None
    """When the document upload was last updated"""


class AccountHolderDocumentUpdatedWebhookEvent(BaseModel):
    event_type: Literal["account_holder_document.updated"]
    """The type of event that occurred."""

    token: Optional[str] = None
    """The token of the account holder document"""

    account_holder_token: Optional[str] = None
    """The token of the account_holder that the document belongs to"""

    created: Optional[datetime] = None
    """When the account_holder was created"""

    document_type: Optional[
        Literal[
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
    ] = None
    """Type of documentation to be submitted for verification of an account holder"""

    entity_token: Optional[str] = None
    """The token of the entity that the document belongs to"""

    required_document_uploads: Optional[List[RequiredDocumentUpload]] = None
