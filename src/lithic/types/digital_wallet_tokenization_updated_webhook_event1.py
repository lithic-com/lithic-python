# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .tokenization import Tokenization

__all__ = ["DigitalWalletTokenizationUpdatedWebhookEvent"]


class DigitalWalletTokenizationUpdatedWebhookEvent(BaseModel):
    account_token: str
    """Account token"""

    card_token: str
    """Card token"""

    created: datetime
    """Created date"""

    event_type: Literal["digital_wallet.tokenization_updated"]
    """The type of event that occurred."""

    tokenization: Tokenization
