# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "ReportStats",
    "Example",
    "ExampleAction",
    "ExampleActionDeclineActionAuthorization",
    "ExampleActionChallengeActionAuthorization",
    "ExampleActionResultAuthentication3DSAction",
    "ExampleActionDeclineActionTokenization",
    "ExampleActionRequireTfaAction",
    "ExampleActionApproveActionACH",
    "ExampleActionReturnAction",
]


class ExampleActionDeclineActionAuthorization(BaseModel):
    code: Literal[
        "ACCOUNT_DAILY_SPEND_LIMIT_EXCEEDED",
        "ACCOUNT_DELINQUENT",
        "ACCOUNT_INACTIVE",
        "ACCOUNT_LIFETIME_SPEND_LIMIT_EXCEEDED",
        "ACCOUNT_MONTHLY_SPEND_LIMIT_EXCEEDED",
        "ACCOUNT_PAUSED",
        "ACCOUNT_UNDER_REVIEW",
        "ADDRESS_INCORRECT",
        "APPROVED",
        "AUTH_RULE_ALLOWED_COUNTRY",
        "AUTH_RULE_ALLOWED_MCC",
        "AUTH_RULE_BLOCKED_COUNTRY",
        "AUTH_RULE_BLOCKED_MCC",
        "AUTH_RULE",
        "CARD_CLOSED",
        "CARD_CRYPTOGRAM_VALIDATION_FAILURE",
        "CARD_EXPIRED",
        "CARD_EXPIRY_DATE_INCORRECT",
        "CARD_INVALID",
        "CARD_NOT_ACTIVATED",
        "CARD_PAUSED",
        "CARD_PIN_INCORRECT",
        "CARD_RESTRICTED",
        "CARD_SECURITY_CODE_INCORRECT",
        "CARD_SPEND_LIMIT_EXCEEDED",
        "CONTACT_CARD_ISSUER",
        "CUSTOMER_ASA_TIMEOUT",
        "CUSTOM_ASA_RESULT",
        "DECLINED",
        "DO_NOT_HONOR",
        "DRIVER_NUMBER_INVALID",
        "FORMAT_ERROR",
        "INSUFFICIENT_FUNDING_SOURCE_BALANCE",
        "INSUFFICIENT_FUNDS",
        "LITHIC_SYSTEM_ERROR",
        "LITHIC_SYSTEM_RATE_LIMIT",
        "MALFORMED_ASA_RESPONSE",
        "MERCHANT_INVALID",
        "MERCHANT_LOCKED_CARD_ATTEMPTED_ELSEWHERE",
        "MERCHANT_NOT_PERMITTED",
        "OVER_REVERSAL_ATTEMPTED",
        "PIN_BLOCKED",
        "PROGRAM_CARD_SPEND_LIMIT_EXCEEDED",
        "PROGRAM_SUSPENDED",
        "PROGRAM_USAGE_RESTRICTION",
        "REVERSAL_UNMATCHED",
        "SECURITY_VIOLATION",
        "SINGLE_USE_CARD_REATTEMPTED",
        "SUSPECTED_FRAUD",
        "TRANSACTION_INVALID",
        "TRANSACTION_NOT_PERMITTED_TO_ACQUIRER_OR_TERMINAL",
        "TRANSACTION_NOT_PERMITTED_TO_ISSUER_OR_CARDHOLDER",
        "TRANSACTION_PREVIOUSLY_COMPLETED",
        "UNAUTHORIZED_MERCHANT",
        "VEHICLE_NUMBER_INVALID",
        "CARDHOLDER_CHALLENGED",
        "CARDHOLDER_CHALLENGE_FAILED",
    ]
    """The detailed result code explaining the specific reason for the decline"""

    type: Literal["DECLINE"]


class ExampleActionChallengeActionAuthorization(BaseModel):
    type: Literal["CHALLENGE"]


class ExampleActionResultAuthentication3DSAction(BaseModel):
    type: Literal["DECLINE", "CHALLENGE"]


class ExampleActionDeclineActionTokenization(BaseModel):
    type: Literal["DECLINE"]
    """Decline the tokenization request"""

    reason: Optional[
        Literal[
            "ACCOUNT_SCORE_1",
            "DEVICE_SCORE_1",
            "ALL_WALLET_DECLINE_REASONS_PRESENT",
            "WALLET_RECOMMENDED_DECISION_RED",
            "CVC_MISMATCH",
            "CARD_EXPIRY_MONTH_MISMATCH",
            "CARD_EXPIRY_YEAR_MISMATCH",
            "CARD_INVALID_STATE",
            "CUSTOMER_RED_PATH",
            "INVALID_CUSTOMER_RESPONSE",
            "NETWORK_FAILURE",
            "GENERIC_DECLINE",
            "DIGITAL_CARD_ART_REQUIRED",
        ]
    ] = None
    """Reason code for declining the tokenization request"""


class ExampleActionRequireTfaAction(BaseModel):
    type: Literal["REQUIRE_TFA"]
    """Require two-factor authentication for the tokenization request"""

    reason: Optional[
        Literal[
            "WALLET_RECOMMENDED_TFA",
            "SUSPICIOUS_ACTIVITY",
            "DEVICE_RECENTLY_LOST",
            "TOO_MANY_RECENT_ATTEMPTS",
            "TOO_MANY_RECENT_TOKENS",
            "TOO_MANY_DIFFERENT_CARDHOLDERS",
            "OUTSIDE_HOME_TERRITORY",
            "HAS_SUSPENDED_TOKENS",
            "HIGH_RISK",
            "ACCOUNT_SCORE_LOW",
            "DEVICE_SCORE_LOW",
            "CARD_STATE_TFA",
            "HARDCODED_TFA",
            "CUSTOMER_RULE_TFA",
            "DEVICE_HOST_CARD_EMULATION",
        ]
    ] = None
    """Reason code for requiring two-factor authentication"""


class ExampleActionApproveActionACH(BaseModel):
    type: Literal["APPROVE"]
    """Approve the ACH transaction"""


class ExampleActionReturnAction(BaseModel):
    code: Literal[
        "R01",
        "R02",
        "R03",
        "R04",
        "R05",
        "R06",
        "R07",
        "R08",
        "R09",
        "R10",
        "R11",
        "R12",
        "R13",
        "R14",
        "R15",
        "R16",
        "R17",
        "R18",
        "R19",
        "R20",
        "R21",
        "R22",
        "R23",
        "R24",
        "R25",
        "R26",
        "R27",
        "R28",
        "R29",
        "R30",
        "R31",
        "R32",
        "R33",
        "R34",
        "R35",
        "R36",
        "R37",
        "R38",
        "R39",
        "R40",
        "R41",
        "R42",
        "R43",
        "R44",
        "R45",
        "R46",
        "R47",
        "R50",
        "R51",
        "R52",
        "R53",
        "R61",
        "R62",
        "R67",
        "R68",
        "R69",
        "R70",
        "R71",
        "R72",
        "R73",
        "R74",
        "R75",
        "R76",
        "R77",
        "R80",
        "R81",
        "R82",
        "R83",
        "R84",
        "R85",
    ]
    """NACHA return code to use when returning the transaction.

    Note that the list of available return codes is subject to an allowlist
    configured at the program level
    """

    type: Literal["RETURN"]
    """Return the ACH transaction"""


ExampleAction: TypeAlias = Union[
    ExampleActionDeclineActionAuthorization,
    ExampleActionChallengeActionAuthorization,
    ExampleActionResultAuthentication3DSAction,
    ExampleActionDeclineActionTokenization,
    ExampleActionRequireTfaAction,
    ExampleActionApproveActionACH,
    ExampleActionReturnAction,
]


class Example(BaseModel):
    actions: Optional[List[ExampleAction]] = None
    """The actions taken by the rule for this event."""

    approved: Optional[bool] = None
    """Whether the rule would have approved the request."""

    decision: Optional[Literal["APPROVED", "DECLINED", "CHALLENGED"]] = None
    """The decision made by the rule for this event."""

    event_token: Optional[str] = None
    """The event token."""

    timestamp: Optional[datetime] = None
    """The timestamp of the event."""

    transaction_token: Optional[str] = None
    """The token of the transaction associated with the event"""


class ReportStats(BaseModel):
    action_counts: Optional[Dict[str, int]] = None
    """
    A mapping of action types to the number of times that action was returned by
    this rule during the relevant period. Actions are the possible outcomes of a
    rule evaluation, such as DECLINE, CHALLENGE, REQUIRE_TFA, etc. In case rule
    didn't trigger any action, it's counted under NO_ACTION key.
    """

    approved: Optional[int] = None
    """
    The total number of historical transactions approved by this rule during the
    relevant period, or the number of transactions that would have been approved if
    the rule was evaluated in shadow mode.
    """

    challenged: Optional[int] = None
    """
    The total number of historical transactions challenged by this rule during the
    relevant period, or the number of transactions that would have been challenged
    if the rule was evaluated in shadow mode. Currently applicable only for 3DS Auth
    Rules.
    """

    declined: Optional[int] = None
    """
    The total number of historical transactions declined by this rule during the
    relevant period, or the number of transactions that would have been declined if
    the rule was evaluated in shadow mode.
    """

    examples: Optional[List[Example]] = None
    """Example events and their outcomes."""
