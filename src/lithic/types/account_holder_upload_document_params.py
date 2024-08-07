# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AccountHolderUploadDocumentParams"]


class AccountHolderUploadDocumentParams(TypedDict, total=False):
    document_type: Literal[
        "EIN_LETTER",
        "TAX_RETURN",
        "OPERATING_AGREEMENT",
        "CERTIFICATE_OF_FORMATION",
        "DRIVERS_LICENSE",
        "PASSPORT",
        "PASSPORT_CARD",
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
    """The type of document to upload"""

    entity_token: str
    """Globally unique identifier for the entity."""
