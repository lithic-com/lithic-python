# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ClaimCreatedWebhookEvent", "DisputedTransaction"]


class DisputedTransaction(BaseModel):
    """
    A transaction included in a claim, along with the specific events being disputed.
    """

    event_tokens: List[str]
    """Tokens for the specific events within the transaction being disputed.

    Lithic creates one dispute per event token
    """

    transaction_token: str
    """Token for the transaction being disputed, in UUID format"""


class ClaimCreatedWebhookEvent(BaseModel):
    token: str
    """Unique identifier for the claim, in UUID format"""

    account_holder_token: Optional[str] = None
    """Token for the account holder that filed the claim"""

    account_token: Optional[str] = None
    """Token for the account associated with the claim"""

    card_tokens: List[str]
    """Tokens for the cards associated with the disputed transactions"""

    created: datetime
    """When the claim was created"""

    disputed_transactions: List[DisputedTransaction]
    """Transactions included in this claim"""

    event_type: Literal["claim.created"]
    """The type of event that occurred."""

    outstanding_requirements: List[Literal["QUESTIONNAIRE", "DOCUMENTS"]]
    """Requirements that must be fulfilled before the claim can be submitted"""

    reason: Literal[
        "CARD_NOT_PRESENT",
        "CARD_LOST",
        "CARD_STOLEN",
        "CARD_NEVER_RECEIVED",
        "COUNTERFEIT",
        "ACCOUNT_TAKEOVER",
        "PRODUCT_NOT_RECEIVED",
        "NOT_AS_DESCRIBED",
        "CREDIT_NOT_PROCESSED",
        "CANCELLED_RECURRING",
        "PAID_BY_OTHER_MEANS",
        "DUPLICATE_CHARGE",
        "LATE_PRESENTMENT",
        "INCORRECT_TRANSACTION_CODE",
        "NO_AUTHORIZATION",
        "DECLINED",
        "INCORRECT_AMOUNT",
        "ATM_CASH_NOT_DISPENSED",
        "ATM_DEPOSIT_WRONG_AMOUNT",
        "ATM_DEPOSIT_MISSING",
    ]
    """Dispute reason code provided when creating the claim"""

    status: Literal["INITIALIZING", "AWAITING_INFO", "SUBMITTED", "RESOLVED", "ABANDONED"]
    """Current lifecycle status of the claim"""

    submitted: Optional[datetime] = None
    """When the claim was submitted. Null until the claim reaches `SUBMITTED` status"""

    updated: datetime
    """When the claim was last updated"""
