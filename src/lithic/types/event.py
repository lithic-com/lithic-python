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
        "account_holder_document.updated",
        "account_holder.created",
        "account_holder.updated",
        "account_holder.verification",
        "auth_rules.backtest_report.created",
        "balance.updated",
        "book_transfer_transaction.created",
        "book_transfer_transaction.updated",
        "card_transaction.enhanced_data.created",
        "card_transaction.enhanced_data.updated",
        "card_transaction.updated",
        "card.converted",
        "card.created",
        "card.reissued",
        "card.renewed",
        "card.shipped",
        "digital_wallet.tokenization_approval_request",
        "digital_wallet.tokenization_result",
        "digital_wallet.tokenization_two_factor_authentication_code",
        "digital_wallet.tokenization_two_factor_authentication_code_sent",
        "digital_wallet.tokenization_updated",
        "dispute_evidence.upload_failed",
        "dispute_transaction.created",
        "dispute_transaction.updated",
        "dispute.updated",
        "external_bank_account.created",
        "external_bank_account.updated",
        "external_payment.created",
        "external_payment.updated",
        "financial_account.created",
        "financial_account.updated",
        "funding_event.created",
        "internal_transaction.created",
        "internal_transaction.updated",
        "loan_tape.created",
        "loan_tape.updated",
        "management_operation.created",
        "management_operation.updated",
        "network_total.created",
        "network_total.updated",
        "payment_transaction.created",
        "payment_transaction.updated",
        "settlement_report.updated",
        "statements.created",
        "three_ds_authentication.challenge",
        "three_ds_authentication.created",
        "three_ds_authentication.updated",
        "tokenization.approval_request",
        "tokenization.result",
        "tokenization.two_factor_authentication_code",
        "tokenization.two_factor_authentication_code_sent",
        "tokenization.updated",
    ]
    """The type of event that occurred. Possible values:

    - account_holder_document.updated: Occurs when an account holder's document
      upload status has been updated
    - account_holder.created: Occurs when a new account_holder is created.
    - account_holder.updated: Occurs when an account_holder is updated.
    - account_holder.verification: Occurs when an asynchronous account_holder's
      verification is completed.
    - auth_rules.backtest_report.created: Auth Rules backtest report created.
    - balance.updated: Financial Account Balance Update
    - book_transfer_transaction.created: Occurs when a book transfer transaction is
      created.
    - book_transfer_transaction.updated: Occurs when a book transfer transaction is
      updated.
    - card_transaction.enhanced_data.created: Occurs when L2/L3 enhanced commercial
      data is processed for a transaction event.
    - card_transaction.enhanced_data.updated: Occurs when L2/L3 enhanced commercial
      data is reprocessed for a transaction event.
    - card_transaction.updated: Occurs when a card transaction happens.
    - card.converted: Occurs when a card is converted from virtual to physical
      cards.
    - card.created: Occurs when a new card is created.
    - card.reissued: Occurs when a card is reissued.
    - card.renewed: Occurs when a card is renewed.
    - card.shipped: Occurs when a card is shipped.
    - digital_wallet.tokenization_approval_request: Occurs when a tokenization
      approval request is made. This event will be deprecated in the future. We
      recommend using `tokenization.approval_request` instead.
    - digital_wallet.tokenization_result: Occurs when a tokenization request
      succeeded or failed.

    This event will be deprecated in the future. We recommend using
    `tokenization.result` instead.

    - digital_wallet.tokenization_two_factor_authentication_code: Occurs when a
      tokenization request 2FA code is sent to the Lithic customer for self serve
      delivery.

    This event will be deprecated in the future. We recommend using
    `tokenization.two_factor_authentication_code` instead.

    - digital_wallet.tokenization_two_factor_authentication_code_sent: Occurs when a
      tokenization request 2FA code is sent to our downstream messaging providers
      for delivery.

    This event will be deprecated in the future. We recommend using
    `tokenization.two_factor_authentication_code_sent` instead.

    - digital_wallet.tokenization_updated: Occurs when a tokenization's status has
      changed.

    This event will be deprecated in the future. We recommend using
    `tokenization.updated` instead.

    - dispute_evidence.upload_failed: Occurs when a dispute evidence upload fails.
    - dispute_transaction.created: Occurs when a new dispute transaction is created
    - dispute_transaction.updated: Occurs when a dispute transaction is updated
    - dispute.updated: Occurs when a dispute is updated.
    - external_bank_account.created: Occurs when an external bank account is
      created.
    - external_bank_account.updated: Occurs when an external bank account is
      updated.
    - external_payment.created: Occurs when an external payment is created.
    - external_payment.updated: Occurs when an external payment is updated.
    - financial_account.created: Occurs when a financial account is created.
    - financial_account.updated: Occurs when a financial account is updated.
    - funding_event.created: Occurs when a funding event is created.
    - internal_transaction.created: Occurs when an internal adjustment is created.
    - internal_transaction.updated: Occurs when an internal adjustment is updated.
    - loan_tape.created: Occurs when a loan tape is created.
    - loan_tape.updated: Occurs when a loan tape is updated.
    - management_operation.created: Occurs when an management operation is created.
    - management_operation.updated: Occurs when an management operation is updated.
    - network_total.created: Occurs when a network total is created.
    - network_total.updated: Occurs when a network total is updated.
    - payment_transaction.created: Occurs when a payment transaction is created.
    - payment_transaction.updated: Occurs when a payment transaction is updated.
    - settlement_report.updated: Occurs when a settlement report is created or
      updated.
    - statements.created: Occurs when a statement has been created
    - three_ds_authentication.challenge: The `three_ds_authentication.challenge`
      event. Upon receiving this request, the Card Program should issue its own
      challenge to the cardholder. After a cardholder challenge is successfully
      completed, the Card Program needs to respond back to Lithic by call to
      [/v1/three_ds_decisioning/challenge_response](https://docs.lithic.com/reference/post_v1-three-ds-decisioning-challenge-response).
      Then the cardholder must navigate back to the merchant checkout flow to
      complete the transaction. Some merchants will include an `app_requestor_url`
      for app-based purchases; Lithic recommends triggering a redirect to that URL
      after the cardholder completes an app-based challenge.
    - three_ds_authentication.created: Occurs when a 3DS authentication is created.
    - three_ds_authentication.updated: Occurs when a 3DS authentication is updated
      (eg. challenge is completed).
    - tokenization.approval_request: Occurs when a tokenization approval request is
      made.
    - tokenization.result: Occurs when a tokenization request succeeded or failed.
    - tokenization.two_factor_authentication_code: Occurs when a tokenization
      request 2FA code is sent to the Lithic customer for self serve delivery.
    - tokenization.two_factor_authentication_code_sent: Occurs when a tokenization
      request 2FA code is sent to our downstream messaging providers for delivery.
    - tokenization.updated: Occurs when a tokenization's status has changed.
    """

    payload: Dict[str, object]
