# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from ..required_document import RequiredDocument

__all__ = ["EntityCreateResponse"]


class EntityCreateResponse(BaseModel):
    """
    Response body for creating a new beneficial owner or replacing the control person entity on an existing KYB account holder.
    """

    token: str
    """Globally unique identifier for the entity"""

    account_holder_token: str
    """Globally unique identifier for the account holder"""

    created: datetime
    """Timestamp of when the entity was created"""

    required_documents: List[RequiredDocument]
    """A list of documents required for the entity to be approved"""

    status: Literal["ACCEPTED", "INACTIVE", "PENDING_REVIEW", "REJECTED"]
    """Entity verification status"""

    status_reasons: List[
        Literal[
            "ADDRESS_VERIFICATION_FAILURE",
            "AGE_THRESHOLD_FAILURE",
            "COMPLETE_VERIFICATION_FAILURE",
            "DOB_VERIFICATION_FAILURE",
            "ID_VERIFICATION_FAILURE",
            "MAX_DOCUMENT_ATTEMPTS",
            "MAX_RESUBMISSION_ATTEMPTS",
            "NAME_VERIFICATION_FAILURE",
            "OTHER_VERIFICATION_FAILURE",
            "RISK_THRESHOLD_FAILURE",
            "WATCHLIST_ALERT_FAILURE",
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
        ]
    ]
    """Reason for the evaluation status"""
