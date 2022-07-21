# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypedDict

__all__ = ["Bank", "Plaid", "FundingSourceCreateParams"]


class Bank(TypedDict, total=False):
    account_number: Required[str]
    """The account number of the bank account."""

    routing_number: Required[str]
    """The routing number of the bank account."""

    validation_method: Required[Literal["BANK"]]

    account_name: str
    """The name associated with the bank account.

    This property is only for identification purposes, and has no bearing on the
    external properties of the bank.
    """

    account_token: str
    """Only required for multi-account users.

    Token identifying the account that the bank account will be associated with.
    Only applicable if using account holder enrollment. See
    [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
    more information.
    """


class Plaid(TypedDict, total=False):
    processor_token: Required[str]
    """The processor token associated with the bank account."""

    validation_method: Required[Literal["PLAID"]]

    account_token: str
    """Only required for multi-account users.

    Token identifying the account associated with the bank account. Only applicable
    if using account holder enrollment. See
    [Managing Your Program](https://docs.lithic.com/docs/managing-your-program) for
    more information.
    """


FundingSourceCreateParams = Union[Bank, Plaid]
