# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .auth_rules.v2.backtest_results import BacktestResults

__all__ = ["AuthRulesBacktestReportCreatedWebhookEvent"]


class AuthRulesBacktestReportCreatedWebhookEvent(BacktestResults):
    event_type: Literal["auth_rules.backtest_report.created"]
    """The type of event that occurred."""
