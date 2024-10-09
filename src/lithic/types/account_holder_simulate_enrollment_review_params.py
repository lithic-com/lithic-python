# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, TypedDict

__all__ = ["AccountHolderSimulateEnrollmentReviewParams"]


class AccountHolderSimulateEnrollmentReviewParams(TypedDict, total=False):
    account_holder_token: str
    """The account holder which to perform the simulation upon."""

    status: Literal["ACCEPTED", "REJECTED"]
    """An account holder's status for use within the simulation."""

    status_reasons: List[
        Literal[
            "PRIMARY_BUSINESS_ENTITY_ID_VERIFICATION_FAILURE",
            "PRIMARY_BUSINESS_ENTITY_ADDRESS_VERIFICATION_FAILURE",
            "PRIMARY_BUSINESS_ENTITY_NAME_VERIFICATION_FAILURE",
            "PRIMARY_BUSINESS_ENTITY_BUSINESS_OFFICERS_NOT_MATCHED",
            "PRIMARY_BUSINESS_ENTITY_SOS_FILING_INACTIVE",
            "PRIMARY_BUSINESS_ENTITY_SOS_NOT_MATCHED",
            "PRIMARY_BUSINESS_ENTITY_CMRA_FAILURE",
            "PRIMARY_BUSINESS_ENTITY_WATCHLIST_FAILURE",
            "PRIMARY_BUSINESS_ENTITY_REGISTERED_AGENT_FAILURE",
            "CONTROL_PERSON_BLOCKLIST_ALERT_FAILURE",
            "CONTROL_PERSON_ID_VERIFICATION_FAILURE",
            "CONTROL_PERSON_DOB_VERIFICATION_FAILURE",
            "CONTROL_PERSON_NAME_VERIFICATION_FAILURE",
            "BENEFICIAL_OWNER_INDIVIDUAL_DOB_VERIFICATION_FAILURE",
            "BENEFICIAL_OWNER_INDIVIDUAL_BLOCKLIST_ALERT_FAILURE",
            "BENEFICIAL_OWNER_INDIVIDUAL_ID_VERIFICATION_FAILURE",
            "BENEFICIAL_OWNER_INDIVIDUAL_NAME_VERIFICATION_FAILURE",
        ]
    ]
    """Status reason that will be associated with the simulated account holder status.

    Only required for a `REJECTED` status.
    """
