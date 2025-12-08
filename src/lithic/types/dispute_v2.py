# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel
from .shared.merchant import Merchant

__all__ = [
    "DisputeV2",
    "Event",
    "EventData",
    "EventDataWorkflow",
    "EventDataFinancial",
    "EventDataCardholderLiability",
    "LiabilityAllocation",
    "TransactionSeries",
]


class EventDataWorkflow(BaseModel):
    """Details specific to workflow events"""

    action: Literal["OPENED", "CLOSED", "REOPENED"]
    """Action taken in this stage"""

    amount: Optional[int] = None
    """Amount in minor units"""

    disposition: Optional[Literal["WON", "LOST", "PARTIALLY_WON", "WITHDRAWN", "DENIED"]] = None
    """Dispute resolution outcome"""

    reason: Optional[str] = None
    """Reason for the action"""

    stage: Literal["CLAIM"]
    """Current stage of the dispute workflow"""

    type: Literal["WORKFLOW"]
    """Event type discriminator"""


class EventDataFinancial(BaseModel):
    """Details specific to financial events"""

    amount: int
    """Amount in minor units"""

    polarity: Literal["CREDIT", "DEBIT"]
    """Direction of funds flow"""

    stage: Literal["CHARGEBACK", "REPRESENTMENT", "PREARBITRATION", "ARBITRATION", "COLLABORATION"]
    """Stage at which the financial event occurred"""

    type: Literal["FINANCIAL"]
    """Event type discriminator"""


class EventDataCardholderLiability(BaseModel):
    """Details specific to cardholder liability events"""

    action: Literal["PROVISIONAL_CREDIT_GRANTED", "PROVISIONAL_CREDIT_REVERSED", "WRITTEN_OFF"]
    """Action taken regarding cardholder liability"""

    amount: int
    """Amount in minor units"""

    reason: str
    """Reason for the action"""

    type: Literal["CARDHOLDER_LIABILITY"]
    """Event type discriminator"""


EventData: TypeAlias = Annotated[
    Union[EventDataWorkflow, EventDataFinancial, EventDataCardholderLiability], PropertyInfo(discriminator="type")
]


class Event(BaseModel):
    """Event that occurred in the dispute lifecycle"""

    token: str
    """Unique identifier for the event, in UUID format"""

    created: datetime
    """When the event occurred"""

    data: EventData
    """Details specific to the event type"""

    type: Literal["WORKFLOW", "FINANCIAL", "CARDHOLDER_LIABILITY"]
    """Type of event"""


class LiabilityAllocation(BaseModel):
    """Current breakdown of how liability is allocated for the disputed amount"""

    denied_amount: int
    """The amount that has been denied to the cardholder"""

    original_amount: int
    """The initial amount disputed"""

    recovered_amount: int
    """
    The amount that has been recovered from the merchant through the dispute process
    """

    remaining_amount: int
    """Any disputed amount that is still outstanding, i.e.

    has not been recovered, written off, or denied
    """

    written_off_amount: int
    """The amount the issuer has chosen to write off"""


class TransactionSeries(BaseModel):
    """
    Contains identifiers for the transaction and specific event within being disputed; null if no transaction can be identified
    """

    related_transaction_event_token: Optional[str] = None
    """
    Token of the specific event in the original transaction being disputed, in UUID
    format; null if no event can be identified
    """

    related_transaction_token: str
    """Token of the original transaction being disputed, in UUID format"""

    type: Literal["DISPUTE"]
    """
    The type of transaction series associating the dispute and the original
    transaction. Always set to DISPUTE
    """


class DisputeV2(BaseModel):
    """
    The Dispute object tracks the progression of a dispute throughout its lifecycle.
    """

    token: str
    """Token assigned by Lithic for the dispute, in UUID format."""

    account_token: str
    """Token for the account associated with the dispute, in UUID format."""

    card_token: str
    """Token for the card used in the dispute, in UUID format."""

    case_id: Optional[str] = None
    """Identifier assigned by the network for this dispute."""

    created: datetime
    """When the dispute was created."""

    currency: str
    """Three-letter ISO 4217 currency code."""

    disposition: Optional[Literal["WON", "LOST", "PARTIALLY_WON", "WITHDRAWN", "DENIED"]] = None
    """Dispute resolution outcome"""

    events: List[Event]
    """Chronological list of events that have occurred in the dispute lifecycle"""

    liability_allocation: LiabilityAllocation
    """Current breakdown of how liability is allocated for the disputed amount"""

    merchant: Merchant

    network: Literal["VISA", "MASTERCARD"]
    """Card network handling the dispute."""

    status: Optional[Literal["OPEN", "CLOSED"]] = None
    """Current status of the dispute."""

    transaction_series: Optional[TransactionSeries] = None
    """
    Contains identifiers for the transaction and specific event within being
    disputed; null if no transaction can be identified
    """

    updated: datetime
    """When the dispute was last updated."""
