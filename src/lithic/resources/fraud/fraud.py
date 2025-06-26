# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .transactions import (
    Transactions,
    AsyncTransactions,
    TransactionsWithRawResponse,
    AsyncTransactionsWithRawResponse,
    TransactionsWithStreamingResponse,
    AsyncTransactionsWithStreamingResponse,
)

__all__ = ["Fraud", "AsyncFraud"]


class Fraud(SyncAPIResource):
    @cached_property
    def transactions(self) -> Transactions:
        return Transactions(self._client)

    @cached_property
    def with_raw_response(self) -> FraudWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return FraudWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FraudWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return FraudWithStreamingResponse(self)


class AsyncFraud(AsyncAPIResource):
    @cached_property
    def transactions(self) -> AsyncTransactions:
        return AsyncTransactions(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFraudWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFraudWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFraudWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncFraudWithStreamingResponse(self)


class FraudWithRawResponse:
    def __init__(self, fraud: Fraud) -> None:
        self._fraud = fraud

    @cached_property
    def transactions(self) -> TransactionsWithRawResponse:
        return TransactionsWithRawResponse(self._fraud.transactions)


class AsyncFraudWithRawResponse:
    def __init__(self, fraud: AsyncFraud) -> None:
        self._fraud = fraud

    @cached_property
    def transactions(self) -> AsyncTransactionsWithRawResponse:
        return AsyncTransactionsWithRawResponse(self._fraud.transactions)


class FraudWithStreamingResponse:
    def __init__(self, fraud: Fraud) -> None:
        self._fraud = fraud

    @cached_property
    def transactions(self) -> TransactionsWithStreamingResponse:
        return TransactionsWithStreamingResponse(self._fraud.transactions)


class AsyncFraudWithStreamingResponse:
    def __init__(self, fraud: AsyncFraud) -> None:
        self._fraud = fraud

    @cached_property
    def transactions(self) -> AsyncTransactionsWithStreamingResponse:
        return AsyncTransactionsWithStreamingResponse(self._fraud.transactions)
