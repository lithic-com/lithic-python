# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .owner_type import OwnerType

__all__ = ["BlockchainRecipient"]


class BlockchainRecipient(BaseModel):
    token: str
    """A globally unique identifier for this blockchain recipient"""

    account_token: Optional[str] = None
    """
    The financial account the blockchain recipient belongs to, or null when the
    recipient is registered against the program rather than a financial account
    """

    address_tag: Optional[str] = None
    """
    An optional tag or memo used by some chains to identify the destination of a
    transfer within a shared address
    """

    chain: str
    """The blockchain network that the address belongs to"""

    created: datetime
    """An ISO 8601 string representing when this blockchain recipient was created"""

    external_id: Optional[str] = None
    """The identifier the recipient is registered under with the payment provider"""

    name: Optional[str] = None
    """The nickname for this blockchain recipient"""

    owner: str
    """Legal name of the business or individual who owns the blockchain address"""

    owner_type: OwnerType
    """Owner Type"""

    program_id: str
    """
    Globally unique identifier for the program the blockchain recipient is
    associated with
    """

    state: Literal["ENABLED", "CLOSED", "PAUSED"]
    """Account State"""

    updated: datetime
    """An ISO 8601 string representing when this blockchain recipient was last updated"""

    verification_state: Literal["PENDING", "ENABLED", "FAILED_VERIFICATION", "INSUFFICIENT_FUNDS"]
    """Verification State"""
