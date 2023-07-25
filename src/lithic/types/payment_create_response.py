# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ..types import balance, financial_transaction
from .._models import BaseModel

__all__ = ["PaymentCreateResponse", "PaymentCreateResponseMethodAttributes"]


class PaymentCreateResponseMethodAttributes(BaseModel):
    sec_code: Literal["PPD", "CCD", "WEB"]


class PaymentCreateResponse(financial_transaction.FinancialTransaction):
    direction: Literal["CREDIT", "DEBIT"]

    method: Literal["ACH_NEXT_DAY", "ACH_SAME_DAY"]

    method_attributes: PaymentCreateResponseMethodAttributes

    source: Literal["LITHIC", "CUSTOMER"]

    balance: Optional[balance.Balance]
    """Balance of a Financial Account"""

    external_bank_account_token: Optional[str]

    user_defined_id: Optional[str]
