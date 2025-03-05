# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EventListParams"]


class EventListParams(TypedDict, total=False):
    begin: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created after the specified time will be included. UTC time zone.
    """

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created before the specified time will be included. UTC time zone.
    """

    ending_before: str
    """A cursor representing an item's token before which a page of results should end.

    Used to retrieve the previous page of results before this item.
    """

    event_types: List[
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
    """Event types to filter events by."""

    page_size: int
    """Page size (for pagination)."""

    starting_after: str
    """A cursor representing an item's token after which a page of results should
    begin.

    Used to retrieve the next page of results after this item.
    """

    with_content: bool
    """Whether to include the event payload content in the response."""
