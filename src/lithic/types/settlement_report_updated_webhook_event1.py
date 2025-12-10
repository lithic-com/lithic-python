# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .settlement_report import SettlementReport

__all__ = ["SettlementReportUpdatedWebhookEvent"]


class SettlementReportUpdatedWebhookEvent(SettlementReport):
    event_type: Literal["settlement_report.updated"]
    """The type of event that occurred."""
