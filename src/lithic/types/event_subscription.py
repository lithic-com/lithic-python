# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["EventSubscription"]


class EventSubscription(BaseModel):
    token: str
    """Globally unique identifier."""

    description: str
    """A description of the subscription."""

    disabled: bool
    """Whether the subscription is disabled."""

    event_types: Optional[
        List[
            Literal[
                "card.created",
                "card.shipped",
                "card_transaction.updated",
                "digital_wallet.tokenization_approval_request",
                "digital_wallet.tokenization_two_factor_authentication_code",
                "dispute.updated",
            ]
        ]
    ]

    url: str
