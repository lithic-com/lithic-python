# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Dispute"]


class Dispute(BaseModel):
    token: str
    """Globally unique identifier."""

    amount: int
    """Amount under dispute. May be different from the original transaction amount."""

    arbitration_date: Optional[datetime] = None
    """Date dispute entered arbitration."""

    created: datetime
    """Timestamp of when first Dispute was reported."""

    customer_filed_date: Optional[datetime] = None
    """Date that the dispute was filed by the customer making the dispute."""

    customer_note: Optional[str] = None
    """End customer description of the reason for the dispute."""

    network_claim_ids: Optional[List[str]] = None
    """Unique identifiers for the dispute from the network."""

    network_filed_date: Optional[datetime] = None
    """Date that the dispute was submitted to the network."""

    network_reason_code: Optional[str] = None
    """Network reason code used to file the dispute."""

    prearbitration_date: Optional[datetime] = None
    """Date dispute entered pre-arbitration."""

    primary_claim_id: Optional[str] = None
    """Unique identifier for the dispute from the network.

    If there are multiple, this will be the first claim id set by the network
    """

    reason: Literal[
        "ATM_CASH_MISDISPENSE",
        "CANCELLED",
        "DUPLICATED",
        "FRAUD_CARD_NOT_PRESENT",
        "FRAUD_CARD_PRESENT",
        "FRAUD_OTHER",
        "GOODS_SERVICES_NOT_AS_DESCRIBED",
        "GOODS_SERVICES_NOT_RECEIVED",
        "INCORRECT_AMOUNT",
        "MISSING_AUTH",
        "OTHER",
        "PROCESSING_ERROR",
        "RECURRING_TRANSACTION_NOT_CANCELLED",
        "REFUND_NOT_PROCESSED",
    ]
    """Dispute reason:

    - `ATM_CASH_MISDISPENSE`: ATM cash misdispense.
    - `CANCELLED`: Transaction was cancelled by the customer.
    - `DUPLICATED`: The transaction was a duplicate.
    - `FRAUD_CARD_NOT_PRESENT`: Fraudulent transaction, card not present.
    - `FRAUD_CARD_PRESENT`: Fraudulent transaction, card present.
    - `FRAUD_OTHER`: Fraudulent transaction, other types such as questionable
      merchant activity.
    - `GOODS_SERVICES_NOT_AS_DESCRIBED`: The goods or services were not as
      described.
    - `GOODS_SERVICES_NOT_RECEIVED`: The goods or services were not received.
    - `INCORRECT_AMOUNT`: The transaction amount was incorrect.
    - `MISSING_AUTH`: The transaction was missing authorization.
    - `OTHER`: Other reason.
    - `PROCESSING_ERROR`: Processing error.
    - `REFUND_NOT_PROCESSED`: The refund was not processed.
    - `RECURRING_TRANSACTION_NOT_CANCELLED`: The recurring transaction was not
      cancelled.
    """

    representment_date: Optional[datetime] = None
    """Date the representment was received."""

    resolution_amount: Optional[int] = None
    """Resolution amount net of network fees."""

    resolution_date: Optional[datetime] = None
    """Date that the dispute was resolved."""

    resolution_note: Optional[str] = None
    """Note by Dispute team on the case resolution."""

    resolution_reason: Optional[
        Literal[
            "CASE_LOST",
            "NETWORK_REJECTED",
            "NO_DISPUTE_RIGHTS_3DS",
            "NO_DISPUTE_RIGHTS_BELOW_THRESHOLD",
            "NO_DISPUTE_RIGHTS_CONTACTLESS",
            "NO_DISPUTE_RIGHTS_HYBRID",
            "NO_DISPUTE_RIGHTS_MAX_CHARGEBACKS",
            "NO_DISPUTE_RIGHTS_OTHER",
            "PAST_FILING_DATE",
            "PREARBITRATION_REJECTED",
            "PROCESSOR_REJECTED_OTHER",
            "REFUNDED",
            "REFUNDED_AFTER_CHARGEBACK",
            "WITHDRAWN",
            "WON_ARBITRATION",
            "WON_FIRST_CHARGEBACK",
            "WON_PREARBITRATION",
        ]
    ] = None
    """Reason for the dispute resolution:

    - `CASE_LOST`: This case was lost at final arbitration.
    - `NETWORK_REJECTED`: Network rejected.
    - `NO_DISPUTE_RIGHTS_3DS`: No dispute rights, 3DS.
    - `NO_DISPUTE_RIGHTS_BELOW_THRESHOLD`: No dispute rights, below threshold.
    - `NO_DISPUTE_RIGHTS_CONTACTLESS`: No dispute rights, contactless.
    - `NO_DISPUTE_RIGHTS_HYBRID`: No dispute rights, hybrid.
    - `NO_DISPUTE_RIGHTS_MAX_CHARGEBACKS`: No dispute rights, max chargebacks.
    - `NO_DISPUTE_RIGHTS_OTHER`: No dispute rights, other.
    - `PAST_FILING_DATE`: Past filing date.
    - `PREARBITRATION_REJECTED`: Prearbitration rejected.
    - `PROCESSOR_REJECTED_OTHER`: Processor rejected, other.
    - `REFUNDED`: Refunded.
    - `REFUNDED_AFTER_CHARGEBACK`: Refunded after chargeback.
    - `WITHDRAWN`: Withdrawn.
    - `WON_ARBITRATION`: Won arbitration.
    - `WON_FIRST_CHARGEBACK`: Won first chargeback.
    - `WON_PREARBITRATION`: Won prearbitration.
    """

    status: Literal[
        "ARBITRATION",
        "CASE_CLOSED",
        "CASE_WON",
        "NEW",
        "PENDING_CUSTOMER",
        "PREARBITRATION",
        "REPRESENTMENT",
        "SUBMITTED",
    ]
    """Status types:

    - `NEW` - New dispute case is opened.
    - `PENDING_CUSTOMER` - Lithic is waiting for customer to provide more
      information.
    - `SUBMITTED` - Dispute is submitted to the card network.
    - `REPRESENTMENT` - Case has entered second presentment.
    - `PREARBITRATION` - Case has entered prearbitration.
    - `ARBITRATION` - Case has entered arbitration.
    - `CASE_WON` - Case was won and credit will be issued.
    - `CASE_CLOSED` - Case was lost or withdrawn.
    """

    transaction_token: str
    """The transaction that is being disputed.

    A transaction can only be disputed once but may have multiple dispute cases.
    """
