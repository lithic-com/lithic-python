# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations
from typing import Optional, Union, List
from typing_extensions import Literal, TypedDict, Required
from ..types import shared_params

__all__ = ["Bank", "Plaid", "FundingSourceCreateParams"]


class Bank(TypedDict, total=False):
    account_number: Required[str]
    """The account number of the bank account."""

    routing_number: Required[str]
    """The routing number of the bank account."""

    validation_method: Required[str]

    account_name: str
    """The name associated with the bank account. This property is only for identification purposes, and has no bearing on the external properties of the bank."""

    account_token: str
    """Only required for multi-account users. Token identifying the account that the bank account will be associated with. Only applicable if using account enrollment. See [Managing Accounts](https://docs.lithic.com/docs/managing-accounts) for more information."""


class Plaid(TypedDict, total=False):
    processor_token: Required[str]
    """The processor token associated with the bank account."""

    validation_method: Required[str]

    account_token: str
    """Only required for multi-account users. Token identifying the account associated with the bank account. Only applicable if using account creation. See [Managing Accounts](https://docs.lithic.com/docs/managing-accounts) for more information."""


FundingSourceCreateParams = Union[Bank, Plaid]
