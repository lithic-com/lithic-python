# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel
from .conditional_value import ConditionalValue
from .conditional_operation import ConditionalOperation

__all__ = ["Conditional3DSActionParameters", "Condition"]


class Condition(BaseModel):
    attribute: Literal[
        "MCC",
        "COUNTRY",
        "CURRENCY",
        "MERCHANT_ID",
        "DESCRIPTOR",
        "TRANSACTION_AMOUNT",
        "RISK_SCORE",
        "MESSAGE_CATEGORY",
        "ADDRESS_MATCH",
        "CARD_STATE",
        "CARD_TYPE",
        "CARD_PROGRAM_FAMILY",
        "PIN_STATUS",
        "CARD_AGE",
    ]
    """The attribute to target.

    The following attributes may be targeted:

    - `MCC`: A four-digit number listed in ISO 18245. An MCC is used to classify a
      business by the types of goods or services it provides.
    - `COUNTRY`: Country of entity of card acceptor. Possible values are: (1) all
      ISO 3166-1 alpha-3 country codes, (2) QZZ for Kosovo, and (3) ANT for
      Netherlands Antilles.
    - `CURRENCY`: 3-character alphabetic ISO 4217 code for the merchant currency of
      the transaction.
    - `MERCHANT_ID`: Unique alphanumeric identifier for the payment card acceptor
      (merchant).
    - `DESCRIPTOR`: Short description of card acceptor.
    - `TRANSACTION_AMOUNT`: The base transaction amount (in cents) plus the acquirer
      fee field in the settlement/cardholder billing currency. This is the amount
      the issuer should authorize against unless the issuer is paying the acquirer
      fee on behalf of the cardholder. Use an integer value.
    - `RISK_SCORE`: Mastercard, and Visa in some markets: Assessment by the network
      of the authentication risk level, with a higher value indicating a higher
      amount of risk. Use an integer value.
    - `MESSAGE_CATEGORY`: The category of the authentication being processed.
    - `ADDRESS_MATCH`: Lithic's evaluation result comparing transaction's address
      data with the cardholder KYC data if it exists. Valid values are `MATCH`,
      `MATCH_ADDRESS_ONLY`, `MATCH_ZIP_ONLY`,`MISMATCH`,`NOT_PRESENT`.
    - `CARD_STATE`: The current state of the card associated with the
      authentication. Valid values are `CLOSED`, `OPEN`, `PAUSED`,
      `PENDING_ACTIVATION`, `PENDING_FULFILLMENT`.
    - `CARD_TYPE`: The type of the card associated with the authentication. Valid
      values are `MERCHANT_LOCKED`, `PHYSICAL`, `SINGLE_USE`, `VIRTUAL`.
    - `CARD_PROGRAM_FAMILY`: The program family of the card associated with the
      authentication. Valid values are `CONSUMER`, `COMMERCIAL`.
    - `PIN_STATUS`: The current state of card's PIN. Valid values are `NOT_SET`,
      `OK`, `BLOCKED`.
    - `CARD_AGE`: The age of the card in seconds at the time of the authentication.
      Use an integer value.
    """

    operation: ConditionalOperation
    """The operation to apply to the attribute"""

    value: ConditionalValue
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class Conditional3DSActionParameters(BaseModel):
    action: Literal["DECLINE", "CHALLENGE"]
    """The action to take if the conditions are met."""

    conditions: List[Condition]
