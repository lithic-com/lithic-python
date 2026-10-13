# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Literal, Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "AuthRuleEntity",
    "AuthRuleProgramEntity",
    "AuthRuleCardEntity",
    "AuthRuleAccountEntity",
    "AuthRuleBusinessAccountEntity",
    "AuthRuleCardTagEntity",
]


class AuthRuleProgramEntity(BaseModel):
    """The entire card program. Takes no other fields."""

    type: Literal["PROGRAM"]


class AuthRuleCardEntity(BaseModel):
    """A single card."""

    token: str
    """Token of the card"""

    type: Literal["CARD"]


class AuthRuleAccountEntity(BaseModel):
    """A single account."""

    token: str
    """Token of the account"""

    type: Literal["ACCOUNT"]


class AuthRuleBusinessAccountEntity(BaseModel):
    """A single business account."""

    token: str
    """Token of the business account"""

    type: Literal["BUSINESS_ACCOUNT"]


class AuthRuleCardTagEntity(BaseModel):
    """Every card whose `tags` contain `key` set to `value`."""

    key: str
    """Tag key.

    Keys starting with `lithic.` (case-insensitive) are reserved and rejected.
    """

    type: Literal["CARD_TAG"]

    value: str
    """Tag value"""


AuthRuleEntity: TypeAlias = Annotated[
    Union[
        AuthRuleProgramEntity,
        AuthRuleCardEntity,
        AuthRuleAccountEntity,
        AuthRuleBusinessAccountEntity,
        AuthRuleCardTagEntity,
    ],
    PropertyInfo(discriminator="type"),
]
