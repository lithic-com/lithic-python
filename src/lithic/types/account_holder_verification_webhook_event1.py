# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AccountHolderVerificationWebhookEvent"]


class AccountHolderVerificationWebhookEvent(BaseModel):
    event_type: Literal["account_holder.verification"]
    """The type of event that occurred."""

    token: Optional[str] = None
    """The token of the account_holder being verified."""

    account_token: Optional[str] = None
    """The token of the account being verified."""

    created: Optional[datetime] = None
    """When the account_holder verification status was updated"""

    status: Optional[Literal["ACCEPTED", "PENDING_REVIEW", "REJECTED"]] = None
    """The status of the account_holder that was created"""

    status_reasons: Optional[List[str]] = None
