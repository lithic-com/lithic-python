# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .event_stream import EventStream

__all__ = [
    "V2ListResultsResponse",
    "Action",
    "ActionAuthorizationAction",
    "ActionThreeDSAction",
    "ActionDeclineAction",
    "ActionRequireTfaAction",
    "ActionApproveAction",
    "ActionReturnAction",
]


class ActionAuthorizationAction(BaseModel):
    explanation: Optional[str] = None
    """Optional explanation for why this action was taken"""


class ActionThreeDSAction(BaseModel):
    explanation: Optional[str] = None
    """Optional explanation for why this action was taken"""


class ActionDeclineAction(BaseModel):
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


class ActionRequireTfaAction(BaseModel):
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


class ActionApproveAction(BaseModel):
    type: Literal["APPROVE"]
    """Approve the ACH transaction"""


class ActionReturnAction(BaseModel):
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


Action: TypeAlias = Union[
    ActionAuthorizationAction,
    ActionThreeDSAction,
    ActionDeclineAction,
    ActionRequireTfaAction,
    ActionApproveAction,
    ActionReturnAction,
]


class V2ListResultsResponse(BaseModel):
    """Result of an Auth Rule evaluation"""

    token: str
    """Globally unique identifier for the evaluation"""

    actions: List[Action]
    """Actions returned by the rule evaluation"""

    auth_rule_token: str
    """The Auth Rule token"""

    evaluation_time: datetime
    """Timestamp of the rule evaluation"""

    event_stream: EventStream
    """The event stream during which the rule was evaluated"""

    event_token: str
    """Token of the event that triggered the evaluation"""

    mode: Literal["ACTIVE", "INACTIVE"]
    """The state of the Auth Rule"""

    rule_version: int
    """Version of the rule that was evaluated"""
