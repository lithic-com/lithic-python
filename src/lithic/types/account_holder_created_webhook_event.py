# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .required_document import RequiredDocument

__all__ = ["AccountHolderCreatedWebhookEvent"]


class AccountHolderCreatedWebhookEvent(BaseModel):
    event_type: Literal["account_holder.created"]
    """The type of event that occurred."""

    token: Optional[str] = None
    """The token of the account_holder that was created."""

    account_token: Optional[str] = None
    """The token of the account that was created."""

    created: Optional[datetime] = None
    """When the account_holder was created"""

    required_documents: Optional[List[RequiredDocument]] = None

    status: Optional[Literal["ACCEPTED", "PENDING_REVIEW"]] = None
    """The status of the account_holder that was created."""

    status_reason: Optional[List[str]] = None
