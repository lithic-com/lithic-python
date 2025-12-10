# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .tokenization_tfa_reason import TokenizationTfaReason
from .tokenization_rule_result import TokenizationRuleResult

__all__ = ["TokenizationResultWebhookEvent", "TokenizationResultDetails"]


class TokenizationResultDetails(BaseModel):
    """The result of the tokenization request."""

    issuer_decision: str
    """Lithic's tokenization decision."""

    tokenization_decline_reasons: List[
        Literal[
            "ACCOUNT_SCORE_1",
            "ALL_WALLET_DECLINE_REASONS_PRESENT",
            "CARD_EXPIRY_MONTH_MISMATCH",
            "CARD_EXPIRY_YEAR_MISMATCH",
            "CARD_INVALID_STATE",
            "CUSTOMER_RED_PATH",
            "CVC_MISMATCH",
            "DEVICE_SCORE_1",
            "GENERIC_DECLINE",
            "INVALID_CUSTOMER_RESPONSE",
            "NETWORK_FAILURE",
            "WALLET_RECOMMENDED_DECISION_RED",
        ]
    ]
    """List of reasons why the tokenization was declined"""

    customer_decision: Optional[str] = None
    """The customer's tokenization decision if applicable."""

    rule_results: Optional[List[TokenizationRuleResult]] = None
    """Results from rules that were evaluated for this tokenization"""

    token_activated_date_time: Optional[datetime] = None
    """An RFC 3339 timestamp indicating when the tokenization succeeded."""

    tokenization_tfa_reasons: Optional[List[TokenizationTfaReason]] = None
    """List of reasons why two-factor authentication was required"""

    wallet_decision: Optional[str] = None
    """The wallet's recommended decision."""


class TokenizationResultWebhookEvent(BaseModel):
    account_token: str
    """Account token"""

    card_token: str
    """Card token"""

    created: datetime
    """Created date"""

    event_type: Literal["tokenization.result"]
    """The type of event that occurred."""

    tokenization_result_details: TokenizationResultDetails
    """The result of the tokenization request."""

    tokenization_token: str
    """Tokenization token"""
