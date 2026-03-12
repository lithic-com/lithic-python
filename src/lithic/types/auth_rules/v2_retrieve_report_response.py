# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .report_stats import ReportStats

__all__ = [
    "V2RetrieveReportResponse",
    "DailyStatistic",
    "DailyStatisticVersion",
    "DailyStatisticVersionExample",
    "DailyStatisticVersionExampleAction",
    "DailyStatisticVersionExampleActionDeclineActionAuthorization",
    "DailyStatisticVersionExampleActionChallengeActionAuthorization",
    "DailyStatisticVersionExampleActionResultAuthentication3DSAction",
    "DailyStatisticVersionExampleActionDeclineActionTokenization",
    "DailyStatisticVersionExampleActionRequireTfaAction",
    "DailyStatisticVersionExampleActionApproveActionACH",
    "DailyStatisticVersionExampleActionReturnAction",
]


class DailyStatisticVersionExampleActionDeclineActionAuthorization(BaseModel):
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


class DailyStatisticVersionExampleActionChallengeActionAuthorization(BaseModel):
    type: Literal["CHALLENGE"]


class DailyStatisticVersionExampleActionResultAuthentication3DSAction(BaseModel):
    type: Literal["DECLINE", "CHALLENGE"]


class DailyStatisticVersionExampleActionDeclineActionTokenization(BaseModel):
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


class DailyStatisticVersionExampleActionRequireTfaAction(BaseModel):
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


class DailyStatisticVersionExampleActionApproveActionACH(BaseModel):
    type: Literal["APPROVE"]
    """Approve the ACH transaction"""


class DailyStatisticVersionExampleActionReturnAction(BaseModel):
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


DailyStatisticVersionExampleAction: TypeAlias = Union[
    DailyStatisticVersionExampleActionDeclineActionAuthorization,
    DailyStatisticVersionExampleActionChallengeActionAuthorization,
    DailyStatisticVersionExampleActionResultAuthentication3DSAction,
    DailyStatisticVersionExampleActionDeclineActionTokenization,
    DailyStatisticVersionExampleActionRequireTfaAction,
    DailyStatisticVersionExampleActionApproveActionACH,
    DailyStatisticVersionExampleActionReturnAction,
]


class DailyStatisticVersionExample(BaseModel):
    actions: List[DailyStatisticVersionExampleAction]
    """The actions taken by this version for this event."""

    event_token: str
    """The event token."""

    timestamp: datetime.datetime
    """The timestamp of the event."""


class DailyStatisticVersion(BaseModel):
    action_counts: Dict[str, int]
    """
    A mapping of action types to the number of times that action was returned by
    this version during the relevant period. Actions are the possible outcomes of a
    rule evaluation, such as DECLINE, CHALLENGE, REQUIRE_TFA, etc. In case rule
    didn't trigger any action, it's counted under NO_ACTION key.
    """

    examples: List[DailyStatisticVersionExample]
    """Example events and their outcomes for this version."""

    state: Literal["ACTIVE", "SHADOW", "INACTIVE"]
    """The evaluation mode of this version during the reported period."""

    version: int
    """The rule version number."""


class DailyStatistic(BaseModel):
    current_version_statistics: Optional[ReportStats] = None
    """Detailed statistics for the current version of the rule."""

    date: datetime.date
    """The date (UTC) for which the statistics are reported."""

    draft_version_statistics: Optional[ReportStats] = None
    """Detailed statistics for the draft version of the rule."""

    versions: List[DailyStatisticVersion]
    """
    Statistics for each version of the rule that was evaluated during the reported
    day.
    """


class V2RetrieveReportResponse(BaseModel):
    auth_rule_token: str
    """Auth Rule Token"""

    begin: datetime.date
    """The start date (UTC) of the report."""

    daily_statistics: List[DailyStatistic]
    """Daily evaluation statistics for the Auth Rule."""

    end: datetime.date
    """The end date (UTC) of the report."""
