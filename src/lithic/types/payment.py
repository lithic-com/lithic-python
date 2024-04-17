# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .financial_transaction import FinancialTransaction

__all__ = ["Payment", "PaymentMethodAttributes"]


class PaymentMethodAttributes(BaseModel):
    company_id: Optional[str] = None

    receipt_routing_number: Optional[str] = None

    retries: Optional[int] = None

    return_reason_code: Optional[str] = None

    sec_code: Literal["CCD", "PPD", "WEB"]


class Payment(FinancialTransaction):
    direction: Literal["CREDIT", "DEBIT"]

    external_bank_account_token: Optional[str] = None

    financial_account_token: str

    method: Literal["ACH_NEXT_DAY", "ACH_SAME_DAY"]

    method_attributes: PaymentMethodAttributes

    source: Literal["CUSTOMER", "LITHIC"]

    user_defined_id: Optional[str] = None
