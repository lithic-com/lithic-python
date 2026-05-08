# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["SignalsResponse"]


class SignalsResponse(BaseModel):
    """
    Behavioral feature state for a card or account derived from its transaction history.

    Derived statistical features (averages, standard deviations, z-scores) are computed using Welford's online algorithm over approved transactions. Average fields are null when fewer than 5 approved transactions have been recorded. Standard deviation fields are null when fewer than 30 approved transactions have been recorded.

    3DS fields (`three_ds_success_rate`, `three_ds_success_count`, `three_ds_total_count`) are card-scoped and will be null for account responses.

    Raw fields (`seen_countries`, `seen_mccs`, `approved_txn_amount_m2`, etc.) are included so clients can compute their own transaction-specific derivations, such as checking whether a new transaction's country is in `seen_countries` to determine `is_new_country`, or computing a z-score using the raw mean and M2 values.
    """

    approved_txn_amount_m2: Optional[float] = None
    """The Welford M2 accumulator for lifetime approved transaction amounts.

    Used together with `avg_transaction_amount` and `approved_txn_count` to compute
    the z-score of a new transaction amount (variance = M2 / (count - 1)).
    """

    approved_txn_amount_m2_30d: Optional[float] = None
    """
    The Welford M2 accumulator for approved transaction amounts over the last 30
    days.
    """

    approved_txn_amount_m2_7d: Optional[float] = None
    """
    The Welford M2 accumulator for approved transaction amounts over the last 7
    days.
    """

    approved_txn_amount_m2_90d: Optional[float] = None
    """
    The Welford M2 accumulator for approved transaction amounts over the last 90
    days.
    """

    approved_txn_count: Optional[int] = None
    """The total number of approved transactions over the entity's lifetime."""

    approved_txn_count_30d: Optional[int] = None
    """The number of approved transactions in the last 30 days."""

    approved_txn_count_7d: Optional[int] = None
    """The number of approved transactions in the last 7 days."""

    approved_txn_count_90d: Optional[int] = None
    """The number of approved transactions in the last 90 days."""

    avg_transaction_amount: Optional[float] = None
    """The average approved transaction amount over the entity's lifetime, in cents.

    Null if fewer than 5 approved transactions have been recorded.
    """

    avg_transaction_amount_30d: Optional[float] = None
    """The average approved transaction amount over the last 30 days, in cents.

    Null if fewer than 5 approved transactions in window.
    """

    avg_transaction_amount_7d: Optional[float] = None
    """The average approved transaction amount over the last 7 days, in cents.

    Null if fewer than 5 approved transactions in window.
    """

    avg_transaction_amount_90d: Optional[float] = None
    """The average approved transaction amount over the last 90 days, in cents.

    Null if fewer than 5 approved transactions in window.
    """

    distinct_country_count: Optional[int] = None
    """
    The number of distinct merchant countries seen in the entity's transaction
    history.
    """

    distinct_mcc_count: Optional[int] = None
    """The number of distinct MCCs seen in the entity's transaction history."""

    first_txn_at: Optional[datetime] = None
    """
    The timestamp of the first approved transaction for the entity, in ISO 8601
    format.
    """

    is_first_transaction: Optional[bool] = None
    """Whether the entity has no prior transaction history.

    Returns true if no history is found. Null if transaction history exists but a
    first transaction timestamp is unavailable.
    """

    last_cp_country: Optional[str] = None
    """The merchant country of the last card-present transaction."""

    last_cp_postal_code: Optional[str] = None
    """The merchant postal code of the last card-present transaction."""

    last_cp_timestamp: Optional[datetime] = None
    """The timestamp of the last card-present transaction, in ISO 8601 format."""

    last_txn_approved_at: Optional[datetime] = None
    """
    The timestamp of the most recent approved transaction for the entity, in ISO
    8601 format.
    """

    seen_countries: Optional[List[str]] = None
    """The set of merchant countries seen in the entity's transaction history.

    Clients can use this to determine whether a new transaction's country is novel
    (i.e. compute `is_new_country`).
    """

    seen_mccs: Optional[List[str]] = None
    """The set of MCCs seen in the entity's transaction history.

    Clients can use this to determine whether a new transaction's MCC is novel (i.e.
    compute `is_new_mcc`).
    """

    seen_merchants: Optional[List[str]] = None
    """
    The set of card acceptor IDs seen in the card's approved transaction history,
    capped at the 1000 most recently seen. Null for account responses. Clients can
    use this to determine whether a new transaction's merchant is novel (i.e.
    compute `is_new_merchant`).
    """

    stdev_transaction_amount: Optional[float] = None
    """
    The standard deviation of approved transaction amounts over the entity's
    lifetime, in cents. Null if fewer than 30 approved transactions have been
    recorded.
    """

    stdev_transaction_amount_30d: Optional[float] = None
    """
    The standard deviation of approved transaction amounts over the last 30 days, in
    cents. Null if fewer than 30 approved transactions in window.
    """

    stdev_transaction_amount_7d: Optional[float] = None
    """
    The standard deviation of approved transaction amounts over the last 7 days, in
    cents. Null if fewer than 30 approved transactions in window.
    """

    stdev_transaction_amount_90d: Optional[float] = None
    """
    The standard deviation of approved transaction amounts over the last 90 days, in
    cents. Null if fewer than 30 approved transactions in window.
    """

    three_ds_success_count: Optional[int] = None
    """The number of successful 3DS authentications for the card.

    Null for account responses.
    """

    three_ds_success_rate: Optional[float] = None
    """
    The 3DS authentication success rate for the card, as a percentage from 0.0 to
    100.0. Null for account responses.
    """

    three_ds_total_count: Optional[int] = None
    """The total number of 3DS authentication attempts for the card.

    Null for account responses.
    """

    time_since_last_transaction_days: Optional[float] = None
    """The number of days since the last approved transaction on the entity."""
