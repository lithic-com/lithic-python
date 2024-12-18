# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .shared_params.address import Address

__all__ = ["KYCParam", "Individual"]


class Individual(TypedDict, total=False):
    address: Required[Address]
    """
    Individual's current address - PO boxes, UPS drops, and FedEx drops are not
    acceptable; APO/FPO are acceptable. Only USA addresses are currently supported.
    """

    dob: Required[str]
    """Individual's date of birth, as an RFC 3339 date."""

    email: Required[str]
    """
    Individual's email address. If utilizing Lithic for chargeback processing, this
    customer email address may be used to communicate dispute status and resolution.
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


class KYCParam(TypedDict, total=False):
    individual: Required[Individual]
    """
    Information on individual for whom the account is being opened and KYC is being
    run.
    """

    tos_timestamp: Required[str]
    """
    An RFC 3339 timestamp indicating when the account holder accepted the applicable
    legal agreements (e.g., cardholder terms) as agreed upon during API customer's
    implementation with Lithic.
    """

    workflow: Required[Literal["KYC_BASIC", "KYC_BYO"]]
    """Specifies the type of KYC workflow to run."""

    external_id: str
    """
    A user provided id that can be used to link an account holder with an external
    system
    """

    kyc_passed_timestamp: str
    """
    An RFC 3339 timestamp indicating when precomputed KYC was completed on the
    individual with a pass result.

    This field is required only if workflow type is `KYC_BYO`.
    """
