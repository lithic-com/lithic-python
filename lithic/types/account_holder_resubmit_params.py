# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["IndividualAddress", "Individual", "AccountHolderResubmitParams"]


class IndividualAddress(TypedDict, total=False):
    address1: Required[str]
    """Valid deliverable address (no PO boxes)."""

    city: Required[str]
    """Name of city."""

    country: Required[str]
    """Valid country code.

    Only USA is currently supported, entered in uppercase ISO 3166-1 alpha-3
    three-character format.
    """

    postal_code: Required[str]
    """Valid postal code.

    Only USA ZIP codes are currently supported, entered as a five-digit ZIP or
    nine-digit ZIP+4.
    """

    state: Required[str]
    """Valid state code.

    Only USA state codes are currently supported, entered in uppercase ISO 3166-2
    two-character format.
    """

    address2: str
    """Unit or apartment number (if applicable)."""


class Individual(TypedDict, total=False):
    address: Required[IndividualAddress]
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: Required[str]
    """Individual's date of birth, as an ISO 8601 date."""

    email: Required[str]
    """Individual's email address.

    If utilizing Lithic for chargeback processing, this customer email address may
    be used to communicate dispute status and resolution.
    """

    first_name: Required[str]
    """Individual's first name, as it appears on government-issued identity documents."""

    government_id: Required[str]
    """
    Government-issued identification number (required for identity verification and
    compliance with banking regulations). Social Security Numbers (SSN) and
    Individual Taxpayer Identification Numbers (ITIN) are currently supported,
    entered as full nine-digits, with or without hyphens
    """

    last_name: Required[str]
    """Individual's last name, as it appears on government-issued identity documents."""

    phone_number: Required[str]
    """Individual's phone number, entered in E.164 format."""


class AccountHolderResubmitParams(TypedDict, total=False):
    individual: Required[Individual]
    """
    Information on individual for whom the account is being opened and KYC is being
    re-run.
    """

    tos_timestamp: Required[str]
    """
    An ISO 8601 timestamp indicating when the account holder accepted the applicable
    legal agreements (e.g., cardholder terms) as agreed upon during API customer's
    implementation with Lithic.
    """

    workflow: Required[Literal["KYC_ADVANCED"]]
