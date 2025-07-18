# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Conditional3DSActionParameters", "Condition"]


class Condition(BaseModel):
    attribute: Optional[
        Literal[
            "MCC",
            "COUNTRY",
            "CURRENCY",
            "MERCHANT_ID",
            "DESCRIPTOR",
            "TRANSACTION_AMOUNT",
            "RISK_SCORE",
            "MESSAGE_CATEGORY",
        ]
    ] = None
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
      fee on behalf of the cardholder.
    - `RISK_SCORE`: Mastercard only: Assessment by the network of the authentication
      risk level, with a higher value indicating a higher amount of risk.
    - `MESSAGE_CATEGORY`: The category of the authentication being processed.
    """

    operation: Optional[
        Literal["IS_ONE_OF", "IS_NOT_ONE_OF", "MATCHES", "DOES_NOT_MATCH", "IS_GREATER_THAN", "IS_LESS_THAN"]
    ] = None
    """The operation to apply to the attribute"""

    value: Union[str, int, List[str], None] = None
    """A regex string, to be used with `MATCHES` or `DOES_NOT_MATCH`"""


class Conditional3DSActionParameters(BaseModel):
    action: Literal["DECLINE", "CHALLENGE"]
    """The action to take if the conditions are met."""

    conditions: List[Condition]
