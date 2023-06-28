# File generated from our OpenAPI spec by Stainless.

from typing import Dict
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["Event"]


class Event(BaseModel):
    token: str
    """Globally unique identifier."""

    created: datetime
    """An RFC 3339 timestamp for when the event was created. UTC time zone.

    If no timezone is specified, UTC will be used.
    """

    event_type: Literal[
        "card.created",
        "card.shipped",
        "card_transaction.updated",
        "digital_wallet.tokenization_approval_request",
        "digital_wallet.tokenization_two_factor_authentication_code",
        "dispute.updated",
    ]
    """Event types:

    - `card.created` - Notification that a card has been created.
    - `card.shipped` - Physical card shipment notification. See
      https://docs.lithic.com/docs/cards#physical-card-shipped-webhook.
    - `card_transaction.updated` - Transaction Lifecycle webhook. See
      https://docs.lithic.com/docs/transaction-webhooks.
    - `dispute.updated` - A dispute has been updated.
    - `digital_wallet.tokenization_approval_request` - Card network's request to
      Lithic to activate a digital wallet token.
    - `digital_wallet.tokenization_two_factor_authentication_code` - A code to be
      passed to an end user to complete digital wallet authentication. See
      https://docs.lithic.com/docs/tokenization-control#digital-wallet-tokenization-auth-code.
    """

    payload: Dict[str, object]
