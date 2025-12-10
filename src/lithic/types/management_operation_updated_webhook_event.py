# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .management_operation_transaction import ManagementOperationTransaction

__all__ = ["ManagementOperationUpdatedWebhookEvent"]


class ManagementOperationUpdatedWebhookEvent(ManagementOperationTransaction):
    event_type: Literal["management_operation.updated"]
    """The type of event that occurred."""
