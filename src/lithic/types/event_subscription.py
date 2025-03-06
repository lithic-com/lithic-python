# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

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
                "auth_rules.performance_report.created",
                "balance.updated",
                "book_transfer_transaction.created",
                "card.created",
                "card.renewed",
                "card.reissued",
                "card.converted",
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
                "external_payment.created",
                "external_payment.updated",
                "financial_account.created",
                "financial_account.updated",
                "loan_tape.created",
                "loan_tape.updated",
                "management_operation.created",
                "management_operation.updated",
                "payment_transaction.created",
                "payment_transaction.updated",
                "internal_transaction.created",
                "internal_transaction.updated",
                "settlement_report.updated",
                "statements.created",
                "three_ds_authentication.created",
                "three_ds_authentication.updated",
                "tokenization.approval_request",
                "tokenization.result",
                "tokenization.two_factor_authentication_code",
                "tokenization.two_factor_authentication_code_sent",
                "tokenization.updated",
            ]
        ]
    ] = None
