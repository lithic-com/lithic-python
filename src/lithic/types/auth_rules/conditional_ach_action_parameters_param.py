# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .conditional_operation import ConditionalOperation
from .conditional_value_param import ConditionalValueParam

__all__ = ["ConditionalACHActionParametersParam", "Action", "ActionApproveAction", "ActionReturnAction", "Condition"]


class ActionApproveAction(TypedDict, total=False):
    type: Required[Literal["APPROVE"]]
    """Approve the ACH transaction"""


class ActionReturnAction(TypedDict, total=False):
    code: Required[
        Literal[
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
    ]
    """NACHA return code to use when returning the transaction.

    Note that the list of available return codes is subject to an allowlist
    configured at the program level
    """

    type: Required[Literal["RETURN"]]
    """Return the ACH transaction"""


Action: TypeAlias = Union[ActionApproveAction, ActionReturnAction]


class Condition(TypedDict, total=False):
    attribute: Required[Literal["COMPANY_NAME", "COMPANY_ID", "TIMESTAMP", "TRANSACTION_AMOUNT", "SEC_CODE", "MEMO"]]
    """The attribute to target.

    The following attributes may be targeted:

    - `COMPANY_NAME`: The name of the company initiating the ACH transaction.
    - `COMPANY_ID`: The company ID (also known as Standard Entry Class (SEC) Company
      ID) of the entity initiating the ACH transaction.
    - `TIMESTAMP`: The timestamp of the ACH transaction in ISO 8601 format.
    - `TRANSACTION_AMOUNT`: The amount of the ACH transaction in minor units
      (cents).
    - `SEC_CODE`: Standard Entry Class code indicating the type of ACH transaction.
      Valid values include PPD (Prearranged Payment and Deposit Entry), CCD
      (Corporate Credit or Debit Entry), WEB (Internet-Initiated/Mobile Entry), TEL
      (Telephone-Initiated Entry), and others.
    - `MEMO`: Optional memo or description field included with the ACH transaction.
    """

    operation: Required[ConditionalOperation]
    """The operation to apply to the attribute"""

    value: Required[Annotated[ConditionalValueParam, PropertyInfo(format="iso8601")]]
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class ConditionalACHActionParametersParam(TypedDict, total=False):
    action: Required[Action]
    """The action to take if the conditions are met"""

    conditions: Required[Iterable[Condition]]
