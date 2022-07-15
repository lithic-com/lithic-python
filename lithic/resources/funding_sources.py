# File generated from our OpenAPI spec by Stainless.

from typing import Union

from .._types import NOT_GIVEN, Headers, Timeout, NotGiven
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.funding_source import *
from ..types.funding_source_list_params import FundingSourceListParams
from ..types.funding_source_create_params import FundingSourceCreateParams
from ..types.funding_source_update_params import FundingSourceUpdateParams
from ..types.funding_source_verify_params import FundingSourceVerifyParams

__all__ = ["FundingSources", "AsyncFundingSources"]


class FundingSources(SyncAPIResource):
    def create(
        self,
        body: FundingSourceCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> FundingSource:
        """Add a funding source using bank routing and account numbers or via Plaid.

        In the production environment, funding accounts will be set to `PENDING` state
        until micro-deposit validation completes while funding accounts in sandbox will
        be set to `ENABLED` state automatically.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            "/funding_sources",
            body=body,
            options=options,
            cast_to=FundingSource,
        )

    def update(
        self,
        funding_source_token: str,
        body: FundingSourceUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> FundingSource:
        """Update a funding source."""
        options = make_request_options(headers, max_retries, timeout)
        return self._patch(
            f"/funding_sources/{funding_source_token}",
            body=body,
            options=options,
            cast_to=FundingSource,
        )

    def list(
        self,
        query: FundingSourceListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> SyncPage[FundingSource]:
        """List all the funding sources associated with the Lithic account."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/funding_sources",
            page=SyncPage[FundingSource],
            query=query,
            options=options,
            model=FundingSource,
        )

    def verify(
        self,
        funding_source_token: str,
        body: FundingSourceVerifyParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> FundingSource:
        """
        Verify a bank account as a funding source by providing received micro-deposit
        amounts.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(
            f"/funding_sources/{funding_source_token}/verify",
            body=body,
            options=options,
            cast_to=FundingSource,
        )


class AsyncFundingSources(AsyncAPIResource):
    async def create(
        self,
        body: FundingSourceCreateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> FundingSource:
        """Add a funding source using bank routing and account numbers or via Plaid.

        In the production environment, funding accounts will be set to `PENDING` state
        until micro-deposit validation completes while funding accounts in sandbox will
        be set to `ENABLED` state automatically.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            "/funding_sources",
            body=body,
            options=options,
            cast_to=FundingSource,
        )

    async def update(
        self,
        funding_source_token: str,
        body: FundingSourceUpdateParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> FundingSource:
        """Update a funding source."""
        options = make_request_options(headers, max_retries, timeout)
        return await self._patch(
            f"/funding_sources/{funding_source_token}",
            body=body,
            options=options,
            cast_to=FundingSource,
        )

    def list(
        self,
        query: FundingSourceListParams = {},
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> AsyncPaginator[FundingSource, AsyncPage[FundingSource]]:
        """List all the funding sources associated with the Lithic account."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/funding_sources",
            page=AsyncPage[FundingSource],
            query=query,
            options=options,
            model=FundingSource,
        )

    async def verify(
        self,
        funding_source_token: str,
        body: FundingSourceVerifyParams,
        *,
        headers: Union[Headers, NotGiven] = NOT_GIVEN,
        max_retries: Union[int, NotGiven] = NOT_GIVEN,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> FundingSource:
        """
        Verify a bank account as a funding source by providing received micro-deposit
        amounts.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(
            f"/funding_sources/{funding_source_token}/verify",
            body=body,
            options=options,
            cast_to=FundingSource,
        )
