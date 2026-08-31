# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CaseEntity"]


class CaseEntity(BaseModel):
    """The entity a case is associated with"""

    entity_token: Optional[str] = None
    """
    Globally unique identifier for the associated entity: the card token for `CARD`,
    the account token for `ACCOUNT`, and the financial account token for
    `FINANCIAL_ACCOUNT`. Null for `PROGRAM`, which is not scoped to an individual
    entity
    """

    entity_type: Literal["CARD", "ACCOUNT", "FINANCIAL_ACCOUNT", "PROGRAM"]
    """The type of entity a case is associated with:

    - `CARD` - The case is associated with a card
    - `ACCOUNT` - The case is associated with an account
    - `FINANCIAL_ACCOUNT` - The case is associated with a financial account
    - `PROGRAM` - The case is associated with the whole program
    """
