# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .conditional_value import ConditionalValue
from .conditional_operation import ConditionalOperation
from .ach_payment_update_action import ACHPaymentUpdateAction

__all__ = ["ConditionalACHPaymentUpdateActionParameters", "Condition"]


class Condition(BaseModel):
    attribute: Literal[
        "TRANSACTION_AMOUNT",
        "SEC_CODE",
        "RETURN_REASON_CODE",
        "ACCOUNT_AGE",
        "EXTERNAL_BANK_ACCOUNT_AGE",
        "EXTERNAL_BANK_ACCOUNT_VERIFICATION_METHOD",
        "EXTERNAL_BANK_ACCOUNT_VERIFICATION_STATE",
        "EXTERNAL_BANK_ACCOUNT_OWNER_TYPE",
        "ACH_EVENT_TYPE",
    ]
    """The attribute to target.

    The following attributes may be targeted:

    - `TRANSACTION_AMOUNT`: The total amount of the ACH payment in minor units
      (cents), calculated as the sum of the settled and pending amounts. Use an
      integer value.
    - `SEC_CODE`: Standard Entry Class code indicating the type of ACH transaction.
      Valid values include PPD (Prearranged Payment and Deposit Entry), CCD
      (Corporate Credit or Debit Entry), WEB (Internet-Initiated/Mobile Entry), TEL
      (Telephone-Initiated Entry), and others.
    - `RETURN_REASON_CODE`: NACHA return reason code associated with the payment
      (for example, `R01`).
    - `ACCOUNT_AGE`: The age of the account in seconds at the time of the payment.
      Use an integer value. For programs where Lithic does not manage or retain
      account holder data, this attribute does not evaluate.
    - `EXTERNAL_BANK_ACCOUNT_AGE`: The age of the external bank account in seconds
      at the time of the payment. Use an integer value.
    - `EXTERNAL_BANK_ACCOUNT_VERIFICATION_METHOD`: The method used to verify the
      external bank account. Valid values are `MANUAL`, `MICRO_DEPOSIT`, `PRENOTE`,
      `EXTERNALLY_VERIFIED`, or `UNVERIFIED`.
    - `EXTERNAL_BANK_ACCOUNT_VERIFICATION_STATE`: The verification state of the
      external bank account. Valid values are `PENDING`, `ENABLED`,
      `FAILED_VERIFICATION`, or `INSUFFICIENT_FUNDS`.
    - `EXTERNAL_BANK_ACCOUNT_OWNER_TYPE`: The owner type of the external bank
      account. Valid values are `INDIVIDUAL` or `BUSINESS`.
    - `ACH_EVENT_TYPE`: The type of ACH payment event being evaluated. Valid values
      include `ACH_ORIGINATION_INITIATED`, `ACH_ORIGINATION_REVIEWED`,
      `ACH_ORIGINATION_CANCELLED`, `ACH_ORIGINATION_PROCESSED`,
      `ACH_ORIGINATION_SETTLED`, `ACH_ORIGINATION_RELEASED`,
      `ACH_ORIGINATION_REJECTED`, `ACH_RECEIPT_PROCESSED`, `ACH_RECEIPT_SETTLED`,
      `ACH_RECEIPT_RELEASED`, `ACH_RECEIPT_RELEASED_EARLY`, `ACH_RETURN_INITIATED`,
      `ACH_RETURN_PROCESSED`, `ACH_RETURN_SETTLED`, and `ACH_RETURN_REJECTED`.
    """

    operation: ConditionalOperation
    """The operation to apply to the attribute"""

    value: ConditionalValue
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class ConditionalACHPaymentUpdateActionParameters(BaseModel):
    action: ACHPaymentUpdateAction
    """The action to take if the conditions are met."""

    conditions: List[Condition]
