# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["FundingSource"]


class FundingSource(BaseModel):
    created: str
    """
    An ISO 8601 string representing when this funding source was added to the Lithic
    account. This may be `null`. UTC time zone.
    """

    last_four: str
    """The last 4 digits of the account (e.g.

    bank account, debit card) associated with this FundingAccount. This may be null.
    """

    state: Literal["ENABLED", "PENDING", "DELETED"]
    """State of funding source.

    Funding source states:

    - `ENABLED` - The funding account is available to use for card creation and
      transactions.
    - `PENDING` - The funding account is still being verified e.g. bank
      micro-deposits verification.
    - `DELETED` - The founding account has been deleted.
    """

    token: str
    """A globally unique identifier for this FundingAccount."""

    type: Literal["DEPOSITORY_CHECKING", "DEPOSITORY_SAVINGS"]
    """Types of funding source:

    - `DEPOSITORY_CHECKING` - Bank checking account.
    - `DEPOSITORY_SAVINGS` - Bank savings account.
    """

    account_name: Optional[str]
    """Account name identifying the funding source. This may be `null`."""

    nickname: Optional[str]
    """The nickname given to the `FundingAccount` or `null` if it has no nickname."""
