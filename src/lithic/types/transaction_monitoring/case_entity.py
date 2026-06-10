# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CaseEntity"]


class CaseEntity(BaseModel):
    """The entity a case is associated with"""

    entity_token: str
    """Globally unique identifier for the associated entity"""

    entity_type: Literal["CARD", "ACCOUNT"]
    """The type of entity a case is associated with:

    - `CARD` - The case is associated with a card
    - `ACCOUNT` - The case is associated with an account
    """
