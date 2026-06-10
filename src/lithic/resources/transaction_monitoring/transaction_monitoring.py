# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .queues import (
    Queues,
    AsyncQueues,
    QueuesWithRawResponse,
    AsyncQueuesWithRawResponse,
    QueuesWithStreamingResponse,
    AsyncQueuesWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .cases.cases import (
    Cases,
    AsyncCases,
    CasesWithRawResponse,
    AsyncCasesWithRawResponse,
    CasesWithStreamingResponse,
    AsyncCasesWithStreamingResponse,
)

__all__ = ["TransactionMonitoring", "AsyncTransactionMonitoring"]


class TransactionMonitoring(SyncAPIResource):
    @cached_property
    def cases(self) -> Cases:
        return Cases(self._client)

    @cached_property
    def queues(self) -> Queues:
        return Queues(self._client)

    @cached_property
    def with_raw_response(self) -> TransactionMonitoringWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return TransactionMonitoringWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionMonitoringWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return TransactionMonitoringWithStreamingResponse(self)


class AsyncTransactionMonitoring(AsyncAPIResource):
    @cached_property
    def cases(self) -> AsyncCases:
        return AsyncCases(self._client)

    @cached_property
    def queues(self) -> AsyncQueues:
        return AsyncQueues(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTransactionMonitoringWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionMonitoringWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionMonitoringWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncTransactionMonitoringWithStreamingResponse(self)


class TransactionMonitoringWithRawResponse:
    def __init__(self, transaction_monitoring: TransactionMonitoring) -> None:
        self._transaction_monitoring = transaction_monitoring

    @cached_property
    def cases(self) -> CasesWithRawResponse:
        return CasesWithRawResponse(self._transaction_monitoring.cases)

    @cached_property
    def queues(self) -> QueuesWithRawResponse:
        return QueuesWithRawResponse(self._transaction_monitoring.queues)


class AsyncTransactionMonitoringWithRawResponse:
    def __init__(self, transaction_monitoring: AsyncTransactionMonitoring) -> None:
        self._transaction_monitoring = transaction_monitoring

    @cached_property
    def cases(self) -> AsyncCasesWithRawResponse:
        return AsyncCasesWithRawResponse(self._transaction_monitoring.cases)

    @cached_property
    def queues(self) -> AsyncQueuesWithRawResponse:
        return AsyncQueuesWithRawResponse(self._transaction_monitoring.queues)


class TransactionMonitoringWithStreamingResponse:
    def __init__(self, transaction_monitoring: TransactionMonitoring) -> None:
        self._transaction_monitoring = transaction_monitoring

    @cached_property
    def cases(self) -> CasesWithStreamingResponse:
        return CasesWithStreamingResponse(self._transaction_monitoring.cases)

    @cached_property
    def queues(self) -> QueuesWithStreamingResponse:
        return QueuesWithStreamingResponse(self._transaction_monitoring.queues)


class AsyncTransactionMonitoringWithStreamingResponse:
    def __init__(self, transaction_monitoring: AsyncTransactionMonitoring) -> None:
        self._transaction_monitoring = transaction_monitoring

    @cached_property
    def cases(self) -> AsyncCasesWithStreamingResponse:
        return AsyncCasesWithStreamingResponse(self._transaction_monitoring.cases)

    @cached_property
    def queues(self) -> AsyncQueuesWithStreamingResponse:
        return AsyncQueuesWithStreamingResponse(self._transaction_monitoring.queues)
