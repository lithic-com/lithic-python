# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["CardTransactionUpdateAction", "TagAction", "CreateCaseAction"]


class TagAction(BaseModel):
    key: str
    """The key of the tag to apply to the transaction"""

    type: Literal["TAG"]
    """Tag the transaction with key-value metadata"""

    value: str
    """The value of the tag to apply to the transaction"""


class CreateCaseAction(BaseModel):
    queue_token: str
    """The token of the queue to create the case in"""

    scope: Literal["CARD", "ACCOUNT"]
    """The scope of the case to create"""

    type: Literal["CREATE_CASE"]
    """Create a case for the transaction"""


CardTransactionUpdateAction: TypeAlias = Union[TagAction, CreateCaseAction]
