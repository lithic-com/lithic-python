# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = ["CardTransactionUpdateActionParam", "TagAction", "CreateCaseAction"]


class TagAction(TypedDict, total=False):
    key: Required[str]
    """The key of the tag to apply to the transaction"""

    type: Required[Literal["TAG"]]
    """Tag the transaction with key-value metadata"""

    value: Required[str]
    """The value of the tag to apply to the transaction"""


class CreateCaseAction(TypedDict, total=False):
    queue_token: Required[str]
    """The token of the queue to create the case in"""

    scope: Required[Literal["CARD", "ACCOUNT"]]
    """The scope of the case to create"""

    type: Required[Literal["CREATE_CASE"]]
    """Create a case for the transaction"""


CardTransactionUpdateActionParam: TypeAlias = Union[TagAction, CreateCaseAction]
