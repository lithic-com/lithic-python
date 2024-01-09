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

    url: str

    event_types: Optional[
        List[
            Literal[
                "account_holder.created",
                "account_holder.updated",
                "account_holder.verification",
                "balance.updated",
                "card.created",
                "card.renewed",
                "card.shipped",
                "card_transaction.updated",
                "digital_wallet.tokenization_approval_request",
                "digital_wallet.tokenization_result",
                "digital_wallet.tokenization_two_factor_authentication_code",
                "dispute.updated",
                "dispute_evidence.upload_failed",
                "payment_transaction.created",
                "payment_transaction.updated",
                "three_ds_authentication.created",
                "transfer_transaction.created",
            ]
        ]
    ] = None
