# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .event_stream import EventStream
from .velocity_limit_params import VelocityLimitParams
from .merchant_lock_parameters import MerchantLockParameters
from .typescript_code_parameters import TypescriptCodeParameters
from .conditional_block_parameters import ConditionalBlockParameters
from .conditional_3ds_action_parameters import Conditional3DSActionParameters
from .conditional_ach_action_parameters import ConditionalACHActionParameters
from .conditional_tokenization_action_parameters import ConditionalTokenizationActionParameters
from .conditional_authorization_action_parameters import ConditionalAuthorizationActionParameters

__all__ = ["AuthRule", "CurrentVersion", "CurrentVersionParameters", "DraftVersion", "DraftVersionParameters"]

CurrentVersionParameters: TypeAlias = Union[
    ConditionalBlockParameters,
    VelocityLimitParams,
    MerchantLockParameters,
    Conditional3DSActionParameters,
    ConditionalAuthorizationActionParameters,
    ConditionalACHActionParameters,
    ConditionalTokenizationActionParameters,
    TypescriptCodeParameters,
]


class CurrentVersion(BaseModel):
    parameters: CurrentVersionParameters
    """Parameters for the Auth Rule"""

    version: int
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """


DraftVersionParameters: TypeAlias = Union[
    ConditionalBlockParameters,
    VelocityLimitParams,
    MerchantLockParameters,
    Conditional3DSActionParameters,
    ConditionalAuthorizationActionParameters,
    ConditionalACHActionParameters,
    ConditionalTokenizationActionParameters,
    TypescriptCodeParameters,
]


class DraftVersion(BaseModel):
    error: Optional[str] = None
    """An error message if the draft version failed compilation.

    Populated when `state` is `ERROR`, `null` otherwise.
    """

    parameters: DraftVersionParameters
    """Parameters for the Auth Rule"""

    state: Literal["PENDING", "SHADOWING", "ERROR"]
    """The state of the draft version.

    Most rules are created synchronously and the state is immediately `SHADOWING`.
    Rules backed by TypeScript code are compiled asynchronously — the state starts
    as `PENDING` and transitions to `SHADOWING` on success or `ERROR` on failure.

    - `PENDING`: Compilation of the rule is in progress (TypeScript rules only).
    - `SHADOWING`: The draft version is ready and evaluating in shadow mode
      alongside the current active version. It can be promoted to the active
      version.
    - `ERROR`: Compilation of the rule failed. Check the `error` field for details.
    """

    version: int
    """
    The version of the rule, this is incremented whenever the rule's parameters
    change.
    """


class AuthRule(BaseModel):
    token: str
    """Auth Rule Token"""

    account_tokens: List[str]
    """Account tokens to which the Auth Rule applies."""

    business_account_tokens: List[str]
    """Business Account tokens to which the Auth Rule applies."""

    card_tokens: List[str]
    """Card tokens to which the Auth Rule applies."""

    current_version: Optional[CurrentVersion] = None

    draft_version: Optional[DraftVersion] = None

    event_stream: EventStream
    """The event stream during which the rule will be evaluated."""

    lithic_managed: bool
    """Indicates whether this auth rule is managed by Lithic.

    If true, the rule cannot be modified or deleted by the user
    """

    name: Optional[str] = None
    """Auth Rule Name"""

    program_level: bool
    """Whether the Auth Rule applies to all authorizations on the card program."""

    state: Literal["ACTIVE", "INACTIVE"]
    """The state of the Auth Rule"""

    type: Literal["CONDITIONAL_BLOCK", "VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION", "TYPESCRIPT_CODE"]
    """The type of Auth Rule.

    For certain rule types, this determines the event stream during which it will be
    evaluated. For rules that can be applied to one of several event streams, the
    effective one is defined by the separate `event_stream` field.

    - `CONDITIONAL_BLOCK`: Deprecated. Use `CONDITIONAL_ACTION` instead.
      AUTHORIZATION event stream.
    - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
    - `MERCHANT_LOCK`: AUTHORIZATION event stream.
    - `CONDITIONAL_ACTION`: AUTHORIZATION, THREE_DS_AUTHENTICATION, TOKENIZATION,
      ACH_CREDIT_RECEIPT, or ACH_DEBIT_RECEIPT event stream.
    - `TYPESCRIPT_CODE`: AUTHORIZATION, THREE_DS_AUTHENTICATION, TOKENIZATION,
      ACH_CREDIT_RECEIPT, or ACH_DEBIT_RECEIPT event stream.
    """

    excluded_account_tokens: Optional[List[str]] = None
    """Account tokens to which the Auth Rule does not apply."""

    excluded_business_account_tokens: Optional[List[str]] = None
    """Business account tokens to which the Auth Rule does not apply."""

    excluded_card_tokens: Optional[List[str]] = None
    """Card tokens to which the Auth Rule does not apply."""
