# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .. import _legacy_response
from ..types import OwnerType, blockchain_recipient_create_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import to_streamed_response_wrapper, async_to_streamed_response_wrapper
from .._base_client import make_request_options
from ..types.owner_type import OwnerType
from ..types.blockchain_recipient import BlockchainRecipient

__all__ = ["BlockchainRecipients", "AsyncBlockchainRecipients"]


class BlockchainRecipients(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BlockchainRecipientsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return BlockchainRecipientsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlockchainRecipientsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return BlockchainRecipientsWithStreamingResponse(self)

    def create(
        self,
        *,
        account_token: str,
        address: str,
        chain: str,
        owner: str,
        owner_type: OwnerType,
        address_tag: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockchainRecipient:
        """
        Register a blockchain address as a withdrawal destination for a financial
        account

        The recipient is created with a `PENDING` verification state and cannot receive
        a payout until screening of the address completes. Registering an address that
        is already registered to the same financial account returns the existing
        recipient and its current verification state, rather than creating a second one

        Args:
          account_token: The financial account the blockchain recipient belongs to

          address: The blockchain address funds will be withdrawn to

          chain: The blockchain network that the address belongs to

          owner: Legal name of the business or individual who owns the blockchain address

          owner_type: Owner Type

          address_tag: An optional tag or memo used by some chains to identify the destination of a
              transfer within a shared address

          name: The nickname for this blockchain recipient

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/blockchain_recipients",
            body=maybe_transform(
                {
                    "account_token": account_token,
                    "address": address,
                    "chain": chain,
                    "owner": owner,
                    "owner_type": owner_type,
                    "address_tag": address_tag,
                    "name": name,
                },
                blockchain_recipient_create_params.BlockchainRecipientCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlockchainRecipient,
        )


class AsyncBlockchainRecipients(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBlockchainRecipientsWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/lithic-com/lithic-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBlockchainRecipientsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlockchainRecipientsWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/lithic-com/lithic-python#with_streaming_response
        """
        return AsyncBlockchainRecipientsWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_token: str,
        address: str,
        chain: str,
        owner: str,
        owner_type: OwnerType,
        address_tag: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BlockchainRecipient:
        """
        Register a blockchain address as a withdrawal destination for a financial
        account

        The recipient is created with a `PENDING` verification state and cannot receive
        a payout until screening of the address completes. Registering an address that
        is already registered to the same financial account returns the existing
        recipient and its current verification state, rather than creating a second one

        Args:
          account_token: The financial account the blockchain recipient belongs to

          address: The blockchain address funds will be withdrawn to

          chain: The blockchain network that the address belongs to

          owner: Legal name of the business or individual who owns the blockchain address

          owner_type: Owner Type

          address_tag: An optional tag or memo used by some chains to identify the destination of a
              transfer within a shared address

          name: The nickname for this blockchain recipient

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/blockchain_recipients",
            body=await async_maybe_transform(
                {
                    "account_token": account_token,
                    "address": address,
                    "chain": chain,
                    "owner": owner,
                    "owner_type": owner_type,
                    "address_tag": address_tag,
                    "name": name,
                },
                blockchain_recipient_create_params.BlockchainRecipientCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlockchainRecipient,
        )


class BlockchainRecipientsWithRawResponse:
    def __init__(self, blockchain_recipients: BlockchainRecipients) -> None:
        self._blockchain_recipients = blockchain_recipients

        self.create = _legacy_response.to_raw_response_wrapper(
            blockchain_recipients.create,
        )


class AsyncBlockchainRecipientsWithRawResponse:
    def __init__(self, blockchain_recipients: AsyncBlockchainRecipients) -> None:
        self._blockchain_recipients = blockchain_recipients

        self.create = _legacy_response.async_to_raw_response_wrapper(
            blockchain_recipients.create,
        )


class BlockchainRecipientsWithStreamingResponse:
    def __init__(self, blockchain_recipients: BlockchainRecipients) -> None:
        self._blockchain_recipients = blockchain_recipients

        self.create = to_streamed_response_wrapper(
            blockchain_recipients.create,
        )


class AsyncBlockchainRecipientsWithStreamingResponse:
    def __init__(self, blockchain_recipients: AsyncBlockchainRecipients) -> None:
        self._blockchain_recipients = blockchain_recipients

        self.create = async_to_streamed_response_wrapper(
            blockchain_recipients.create,
        )
