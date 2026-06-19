# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["ACHPaymentUpdateAction", "TagAction", "CreateCaseAction"]


class TagAction(BaseModel):
    key: str
    """The key of the tag to apply to the payment"""

    type: Literal["TAG"]
    """Tag the payment with key-value metadata"""

    value: str
    """The value of the tag to apply to the payment"""


class CreateCaseAction(BaseModel):
    queue_token: str
    """The token of the queue to create the case in"""

    scope: Literal["FINANCIAL_ACCOUNT"]
    """The scope of the case to create"""

    type: Literal["CREATE_CASE"]
    """Create a case for the payment"""


ACHPaymentUpdateAction: TypeAlias = Union[TagAction, CreateCaseAction]
