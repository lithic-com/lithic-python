# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["ACHPaymentUpdateActionParam", "TagAction", "CreateCaseAction"]


class TagAction(TypedDict, total=False):
    key: Required[str]
    """The key of the tag to apply to the payment"""

    type: Required[Literal["TAG"]]
    """Tag the payment with key-value metadata"""

    value: Required[str]
    """The value of the tag to apply to the payment"""


class CreateCaseAction(TypedDict, total=False):
    queue_token: Required[str]
    """The token of the queue to create the case in"""

    scope: Required[Literal["FINANCIAL_ACCOUNT"]]
    """The scope of the case to create"""

    type: Required[Literal["CREATE_CASE"]]
    """Create a case for the payment"""


ACHPaymentUpdateActionParam: TypeAlias = Union[TagAction, CreateCaseAction]
