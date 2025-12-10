# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .device import Device
from .._models import BaseModel
from .tokenization_tfa_reason import TokenizationTfaReason
from .wallet_decisioning_info import WalletDecisioningInfo
from .tokenization_rule_result import TokenizationRuleResult
from .tokenization_decline_reason import TokenizationDeclineReason
from .digital_wallet_token_metadata import DigitalWalletTokenMetadata

__all__ = ["DigitalWalletTokenizationApprovalRequestWebhookEvent", "CustomerTokenizationDecision"]


class CustomerTokenizationDecision(BaseModel):
    """Contains the metadata for the customer tokenization decision."""

    outcome: Literal[
        "APPROVED", "DECLINED", "ERROR", "INVALID_RESPONSE", "REQUIRE_ADDITIONAL_AUTHENTICATION", "TIMEOUT"
    ]
    """The outcome of the customer's decision"""

    responder_url: str
    """The customer's subscribed URL"""

    latency: Optional[str] = None
    """Time in ms it took for the customer's URL to respond"""

    response_code: Optional[str] = None
    """The response code that the customer provided"""


class DigitalWalletTokenizationApprovalRequestWebhookEvent(BaseModel):
    account_token: str
    """Unique identifier for the user tokenizing a card"""

    card_token: str
    """Unique identifier for the card being tokenized"""

    created: datetime
    """Indicate when the request was received from Mastercard or Visa"""

    customer_tokenization_decision: Optional[CustomerTokenizationDecision] = None
    """Contains the metadata for the customer tokenization decision."""

    event_type: Literal["digital_wallet.tokenization_approval_request"]
    """The name of this event"""

    issuer_decision: Literal["APPROVED", "DENIED", "VERIFICATION_REQUIRED"]
    """Whether Lithic decisioned on the token, and if so, what the decision was.

    APPROVED/VERIFICATION_REQUIRED/DENIED.
    """

    tokenization_channel: Literal["DIGITAL_WALLET", "MERCHANT"]
    """The channel through which the tokenization was made."""

    tokenization_token: str
    """Unique identifier for the digital wallet token attempt"""

    wallet_decisioning_info: WalletDecisioningInfo

    device: Optional[Device] = None

    digital_wallet_token_metadata: Optional[DigitalWalletTokenMetadata] = None
    """Contains the metadata for the digital wallet being tokenized."""

    rule_results: Optional[List[TokenizationRuleResult]] = None
    """Results from rules that were evaluated for this tokenization"""

    tokenization_decline_reasons: Optional[List[TokenizationDeclineReason]] = None
    """List of reasons why the tokenization was declined"""

    tokenization_source: Optional[
        Literal["ACCOUNT_ON_FILE", "CONTACTLESS_TAP", "MANUAL_PROVISION", "PUSH_PROVISION", "TOKEN", "UNKNOWN"]
    ] = None
    """The source of the tokenization."""

    tokenization_tfa_reasons: Optional[List[TokenizationTfaReason]] = None
    """List of reasons why two-factor authentication was required"""
