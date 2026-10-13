# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from .event_stream import EventStream
from .auth_rule_entities_param import AuthRuleEntitiesParam
from .velocity_limit_params_param import VelocityLimitParamsParam
from .merchant_lock_parameters_param import MerchantLockParametersParam
from .typescript_code_parameters_param import TypescriptCodeParametersParam
from .conditional_3ds_action_parameters_param import Conditional3DSActionParametersParam
from .conditional_ach_action_parameters_param import ConditionalACHActionParametersParam
from .conditional_tokenization_action_parameters_param import ConditionalTokenizationActionParametersParam
from .conditional_authorization_action_parameters_param import ConditionalAuthorizationActionParametersParam
from .conditional_authorization_adjustment_parameters_param import ConditionalAuthorizationAdjustmentParametersParam
from .conditional_ach_payment_update_action_parameters_param import ConditionalACHPaymentUpdateActionParametersParam
from .conditional_card_transaction_update_action_parameters_param import (
    ConditionalCardTransactionUpdateActionParametersParam,
)

__all__ = [
    "V2CreateParams",
    "Rule",
    "RuleParameters",
    "AccountLevelRule",
    "AccountLevelRuleParameters",
    "CardLevelRule",
    "CardLevelRuleParameters",
    "ProgramLevelRule",
    "ProgramLevelRuleParameters",
]


class Rule(TypedDict, total=False):
    entities: Required[AuthRuleEntitiesParam]
    """
    The entities an Auth Rule applies to (`include`) and does not apply to
    (`exclude`). An exclusion overrides an inclusion, so a card excluded here is
    skipped even when the program, its account or one of its tags is included.

    The rule's resulting entities must satisfy these constraints after any write:

    - `include` must contain at least one entity.
    - If `PROGRAM` is included, it must be the only included entity.
    - `PROGRAM` cannot be excluded.
    - An entity cannot appear in both `include` and `exclude`, or twice in the same
      list.
    - A rule can have at most 1,000 entities across `include` and `exclude`, not
      counting `PROGRAM`.
    - Entity types must be valid for the rule's event stream.
    - `CARD`, `ACCOUNT` and `BUSINESS_ACCOUNT` tokens must belong to your program.
    """

    parameters: Required[RuleParameters]
    """Parameters for the Auth Rule"""

    type: Required[Literal["VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION", "TYPESCRIPT_CODE", "OTHER"]]
    """The type of Auth Rule.

    For certain rule types, this determines the event stream during which it will be
    evaluated. For rules that can be applied to one of several event streams, the
    effective one is defined by the separate `event_stream` field.

    - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
    - `MERCHANT_LOCK`: AUTHORIZATION event stream.
    - `CONDITIONAL_ACTION`: AUTHORIZATION, THREE_DS_AUTHENTICATION, TOKENIZATION,
      ACH_CREDIT_RECEIPT, ACH_DEBIT_RECEIPT, CARD_TRANSACTION_UPDATE, or
      ACH_PAYMENT_UPDATE event stream.
    - `TYPESCRIPT_CODE`: AUTHORIZATION, THREE_DS_AUTHENTICATION, TOKENIZATION,
      ACH_CREDIT_RECEIPT, ACH_DEBIT_RECEIPT, CARD_TRANSACTION_UPDATE, or
      ACH_PAYMENT_UPDATE event stream.
    - `OTHER`: A rule whose type is not exposed through this API. Rules of this type
      are read-only; `OTHER` cannot be used when creating a rule.
    """

    event_stream: EventStream
    """The event stream during which the rule will be evaluated."""

    name: Optional[str]
    """Auth Rule Name"""


RuleParameters: TypeAlias = Union[
    VelocityLimitParamsParam,
    MerchantLockParametersParam,
    Conditional3DSActionParametersParam,
    ConditionalAuthorizationActionParametersParam,
    ConditionalACHActionParametersParam,
    ConditionalTokenizationActionParametersParam,
    ConditionalCardTransactionUpdateActionParametersParam,
    ConditionalACHPaymentUpdateActionParametersParam,
    TypescriptCodeParametersParam,
    ConditionalAuthorizationAdjustmentParametersParam,
]


class AccountLevelRule(TypedDict, total=False):
    parameters: Required[AccountLevelRuleParameters]
    """Parameters for the Auth Rule"""

    type: Required[Literal["VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION", "TYPESCRIPT_CODE", "OTHER"]]
    """The type of Auth Rule.

    For certain rule types, this determines the event stream during which it will be
    evaluated. For rules that can be applied to one of several event streams, the
    effective one is defined by the separate `event_stream` field.

    - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
    - `MERCHANT_LOCK`: AUTHORIZATION event stream.
    - `CONDITIONAL_ACTION`: AUTHORIZATION, THREE_DS_AUTHENTICATION, TOKENIZATION,
      ACH_CREDIT_RECEIPT, ACH_DEBIT_RECEIPT, CARD_TRANSACTION_UPDATE, or
      ACH_PAYMENT_UPDATE event stream.
    - `TYPESCRIPT_CODE`: AUTHORIZATION, THREE_DS_AUTHENTICATION, TOKENIZATION,
      ACH_CREDIT_RECEIPT, ACH_DEBIT_RECEIPT, CARD_TRANSACTION_UPDATE, or
      ACH_PAYMENT_UPDATE event stream.
    - `OTHER`: A rule whose type is not exposed through this API. Rules of this type
      are read-only; `OTHER` cannot be used when creating a rule.
    """

    account_tokens: SequenceNotStr[str]
    """Deprecated: Use `entities.include` with `ACCOUNT` entities instead.

    Account tokens to which the Auth Rule applies.
    """

    business_account_tokens: SequenceNotStr[str]
    """Deprecated: Use `entities.include` with `BUSINESS_ACCOUNT` entities instead.

    Business Account tokens to which the Auth Rule applies.
    """

    event_stream: EventStream
    """The event stream during which the rule will be evaluated."""

    name: Optional[str]
    """Auth Rule Name"""


AccountLevelRuleParameters: TypeAlias = Union[
    VelocityLimitParamsParam,
    MerchantLockParametersParam,
    Conditional3DSActionParametersParam,
    ConditionalAuthorizationActionParametersParam,
    ConditionalACHActionParametersParam,
    ConditionalTokenizationActionParametersParam,
    ConditionalCardTransactionUpdateActionParametersParam,
    ConditionalACHPaymentUpdateActionParametersParam,
    TypescriptCodeParametersParam,
    ConditionalAuthorizationAdjustmentParametersParam,
]


class CardLevelRule(TypedDict, total=False):
    card_tokens: Required[SequenceNotStr[str]]
    """Deprecated: Use `entities.include` with `CARD` entities instead.

    Card tokens to which the Auth Rule applies. Cards the rule applies to through a
    `CARD_TAG` entity are not listed.
    """

    parameters: Required[CardLevelRuleParameters]
    """Parameters for the Auth Rule"""

    type: Required[Literal["VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION", "TYPESCRIPT_CODE", "OTHER"]]
    """The type of Auth Rule.

    For certain rule types, this determines the event stream during which it will be
    evaluated. For rules that can be applied to one of several event streams, the
    effective one is defined by the separate `event_stream` field.

    - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
    - `MERCHANT_LOCK`: AUTHORIZATION event stream.
    - `CONDITIONAL_ACTION`: AUTHORIZATION, THREE_DS_AUTHENTICATION, TOKENIZATION,
      ACH_CREDIT_RECEIPT, ACH_DEBIT_RECEIPT, CARD_TRANSACTION_UPDATE, or
      ACH_PAYMENT_UPDATE event stream.
    - `TYPESCRIPT_CODE`: AUTHORIZATION, THREE_DS_AUTHENTICATION, TOKENIZATION,
      ACH_CREDIT_RECEIPT, ACH_DEBIT_RECEIPT, CARD_TRANSACTION_UPDATE, or
      ACH_PAYMENT_UPDATE event stream.
    - `OTHER`: A rule whose type is not exposed through this API. Rules of this type
      are read-only; `OTHER` cannot be used when creating a rule.
    """

    event_stream: EventStream
    """The event stream during which the rule will be evaluated."""

    name: Optional[str]
    """Auth Rule Name"""


CardLevelRuleParameters: TypeAlias = Union[
    VelocityLimitParamsParam,
    MerchantLockParametersParam,
    Conditional3DSActionParametersParam,
    ConditionalAuthorizationActionParametersParam,
    ConditionalACHActionParametersParam,
    ConditionalTokenizationActionParametersParam,
    ConditionalCardTransactionUpdateActionParametersParam,
    ConditionalACHPaymentUpdateActionParametersParam,
    TypescriptCodeParametersParam,
    ConditionalAuthorizationAdjustmentParametersParam,
]


class ProgramLevelRule(TypedDict, total=False):
    parameters: Required[ProgramLevelRuleParameters]
    """Parameters for the Auth Rule"""

    program_level: Required[bool]
    """Deprecated: Use `entities.include` with a `PROGRAM` entity instead.

    Whether the Auth Rule applies to all authorizations on the card program.
    """

    type: Required[Literal["VELOCITY_LIMIT", "MERCHANT_LOCK", "CONDITIONAL_ACTION", "TYPESCRIPT_CODE", "OTHER"]]
    """The type of Auth Rule.

    For certain rule types, this determines the event stream during which it will be
    evaluated. For rules that can be applied to one of several event streams, the
    effective one is defined by the separate `event_stream` field.

    - `VELOCITY_LIMIT`: AUTHORIZATION event stream.
    - `MERCHANT_LOCK`: AUTHORIZATION event stream.
    - `CONDITIONAL_ACTION`: AUTHORIZATION, THREE_DS_AUTHENTICATION, TOKENIZATION,
      ACH_CREDIT_RECEIPT, ACH_DEBIT_RECEIPT, CARD_TRANSACTION_UPDATE, or
      ACH_PAYMENT_UPDATE event stream.
    - `TYPESCRIPT_CODE`: AUTHORIZATION, THREE_DS_AUTHENTICATION, TOKENIZATION,
      ACH_CREDIT_RECEIPT, ACH_DEBIT_RECEIPT, CARD_TRANSACTION_UPDATE, or
      ACH_PAYMENT_UPDATE event stream.
    - `OTHER`: A rule whose type is not exposed through this API. Rules of this type
      are read-only; `OTHER` cannot be used when creating a rule.
    """

    event_stream: EventStream
    """The event stream during which the rule will be evaluated."""

    excluded_account_tokens: SequenceNotStr[str]
    """Deprecated: Use `entities.exclude` with `ACCOUNT` entities instead.

    Account tokens to which the Auth Rule does not apply.
    """

    excluded_business_account_tokens: SequenceNotStr[str]
    """Deprecated: Use `entities.exclude` with `BUSINESS_ACCOUNT` entities instead.

    Business account tokens to which the Auth Rule does not apply.
    """

    excluded_card_tokens: SequenceNotStr[str]
    """Deprecated: Use `entities.exclude` with `CARD` entities instead.

    Card tokens to which the Auth Rule does not apply. Cards excluded through a
    `CARD_TAG` entity are not listed.
    """

    name: Optional[str]
    """Auth Rule Name"""


ProgramLevelRuleParameters: TypeAlias = Union[
    VelocityLimitParamsParam,
    MerchantLockParametersParam,
    Conditional3DSActionParametersParam,
    ConditionalAuthorizationActionParametersParam,
    ConditionalACHActionParametersParam,
    ConditionalTokenizationActionParametersParam,
    ConditionalCardTransactionUpdateActionParametersParam,
    ConditionalACHPaymentUpdateActionParametersParam,
    TypescriptCodeParametersParam,
    ConditionalAuthorizationAdjustmentParametersParam,
]

V2CreateParams: TypeAlias = Union[Rule, AccountLevelRule, CardLevelRule, ProgramLevelRule]
