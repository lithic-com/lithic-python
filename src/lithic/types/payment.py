# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .financial_transaction import FinancialTransaction

__all__ = ["Payment", "PaymentMethodAttributes"]


class PaymentMethodAttributes(BaseModel):
    sec_code: Literal["PPD", "CCD", "WEB"]


class Payment(FinancialTransaction):
    direction: Literal["CREDIT", "DEBIT"]

    method: Literal["ACH_NEXT_DAY", "ACH_SAME_DAY"]

    method_attributes: PaymentMethodAttributes

    source: Literal["LITHIC", "CUSTOMER"]

    external_bank_account_token: Optional[str] = None

    user_defined_id: Optional[str] = None
