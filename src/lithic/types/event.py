# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
    """Event types:

    - `account_holder.created` - Notification that a new account holder has been
      created and was not rejected.
    - `account_holder.updated` - Notification that an account holder was updated.
    - `account_holder.verification` - Notification than an account holder's identity
      verification is complete.
    - `card.created` - Notification that a card has been created.
    - `card.renewed` - Notification that a card has been renewed.
    - `card.shipped` - Physical card shipment notification. See
      https://docs.lithic.com/docs/cards#physical-card-shipped-webhook.
    - `card_transaction.updated` - Transaction Lifecycle webhook. See
      https://docs.lithic.com/docs/transaction-webhooks.
    - `dispute.updated` - A dispute has been updated.
    - `digital_wallet.tokenization_approval_request` - Card network's request to
      Lithic to activate a digital wallet token.
    - `digital_wallet.tokenization_result` - Notification of the end result of a
      tokenization, whether successful or failed.
    - `digital_wallet.tokenization_two_factor_authentication_code` - A code to be
      passed to an end user to complete digital wallet authentication. See
      https://docs.lithic.com/docs/tokenization-control#digital-wallet-tokenization-auth-code.
    - `digital_wallet.tokenization_two_factor_authentication_code_sent` -
      Notification that a two factor authentication code for activating a digital
      wallet has been sent to the end user.
    - `digital_wallet.tokenization_updated` - Notification that a digital wallet
      tokenization's status has changed.
    """

    payload: Dict[str, object]
