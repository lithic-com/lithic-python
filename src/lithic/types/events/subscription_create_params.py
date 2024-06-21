# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["SubscriptionCreateParams"]


class SubscriptionCreateParams(TypedDict, total=False):
    url: Required[str]
    """URL to which event webhooks will be sent. URL must be a valid HTTPS address."""

    description: str
    """Event subscription description."""

    disabled: bool
    """Whether the event subscription is active (false) or inactive (true)."""

    event_types: List[
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
            "digital_wallet.tokenization_two_factor_authentication_code_sent",
            "digital_wallet.tokenization_updated",
            "dispute.updated",
            "dispute_evidence.upload_failed",
            "external_bank_account.created",
            "external_bank_account.updated",
            "financial_account.created",
            "payment_transaction.created",
            "payment_transaction.updated",
            "settlement_report.updated",
            "three_ds_authentication.created",
            "transfer_transaction.created",
        ]
    ]
    """Indicates types of events that will be sent to this subscription.

    If left blank, all types will be sent.
    """
