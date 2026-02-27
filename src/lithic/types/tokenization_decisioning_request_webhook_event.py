# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .device import Device
from .._models import BaseModel
from .token_metadata import TokenMetadata
from .wallet_decisioning_info import WalletDecisioningInfo

__all__ = ["TokenizationDecisioningRequestWebhookEvent"]


class TokenizationDecisioningRequestWebhookEvent(BaseModel):
    """
    A webhook for tokenization decisioning sent to the customer's responder endpoint
    """

    account_token: str
    """Unique identifier for the user tokenizing a card"""

    card_token: str
    """Unique identifier for the card being tokenized"""

    created: datetime
    """Indicate when the request was received from Mastercard or Visa"""

    digital_wallet_token_metadata: TokenMetadata
    """Contains the metadata for the digital wallet being tokenized."""

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

    tokenization_source: Optional[
        Literal["ACCOUNT_ON_FILE", "CONTACTLESS_TAP", "MANUAL_PROVISION", "PUSH_PROVISION", "TOKEN", "UNKNOWN"]
    ] = None
    """The source of the tokenization."""
