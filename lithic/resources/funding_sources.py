# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Union, Optional

from .._types import Timeout, NotGiven
from .._models import NoneModel, StringModel
from .._resource import SyncAPIResource, AsyncAPIResource
from ..pagination import SyncPage, AsyncPage
from .._base_client import AsyncPaginator, make_request_options
from ..types.funding_source import *
from ..types.funding_source_list_params import *
from ..types.funding_source_create_params import *
from ..types.funding_source_update_params import *
from ..types.funding_source_verify_params import *

__all__ = ["FundingSources", "AsyncFundingSources"]


class FundingSources(SyncAPIResource):
    def create(
        self,
        body: FundingSourceCreateParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> FundingSource:
        """Add a funding source using bank routing and account numbers or via Plaid.

        In the production environment, funding accounts will be set to `PENDING` state
        until micro-deposit validation completes while funding accounts in sandbox will
        be set to `ENABLED` state automatically.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post("/funding_sources", model=FundingSource, body=body, options=options)

    def update(
        self,
        id: str,
        body: FundingSourceUpdateParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> FundingSource:
        """Update a funding source."""
        options = make_request_options(headers, max_retries, timeout)
        return self._patch(f"/funding_sources/{id}", model=FundingSource, body=body, options=options)

    def list(
        self,
        query: FundingSourceListParams = {},
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> SyncPage[FundingSource]:
        """List all the funding sources associated with the Lithic account."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/funding_sources", model=FundingSource, page=SyncPage[FundingSource], query=query, options=options
        )

    def verify(
        self,
        id: str,
        body: FundingSourceVerifyParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> FundingSource:
        """
        Verify a bank account as a funding source by providing received micro-deposit
        amounts.
        """
        options = make_request_options(headers, max_retries, timeout)
        return self._post(f"/funding_sources/{id}/verify", model=FundingSource, body=body, options=options)


class AsyncFundingSources(AsyncAPIResource):
    async def create(
        self,
        body: FundingSourceCreateParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> FundingSource:
        """Add a funding source using bank routing and account numbers or via Plaid.

        In the production environment, funding accounts will be set to `PENDING` state
        until micro-deposit validation completes while funding accounts in sandbox will
        be set to `ENABLED` state automatically.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post("/funding_sources", model=FundingSource, body=body, options=options)

    async def update(
        self,
        id: str,
        body: FundingSourceUpdateParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> FundingSource:
        """Update a funding source."""
        options = make_request_options(headers, max_retries, timeout)
        return await self._patch(f"/funding_sources/{id}", model=FundingSource, body=body, options=options)

    def list(
        self,
        query: FundingSourceListParams = {},
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> AsyncPaginator[FundingSource, AsyncPage[FundingSource]]:
        """List all the funding sources associated with the Lithic account."""
        options = make_request_options(headers, max_retries, timeout)
        return self._get_api_list(
            "/funding_sources", model=FundingSource, page=AsyncPage[FundingSource], query=query, options=options
        )

    async def verify(
        self,
        id: str,
        body: FundingSourceVerifyParams,
        *,
        headers: Union[Dict[str, str], NotGiven] = NotGiven(),
        max_retries: Union[int, NotGiven] = NotGiven(),
        timeout: Union[float, Timeout, None, NotGiven] = NotGiven(),
    ) -> FundingSource:
        """
        Verify a bank account as a funding source by providing received micro-deposit
        amounts.
        """
        options = make_request_options(headers, max_retries, timeout)
        return await self._post(f"/funding_sources/{id}/verify", model=FundingSource, body=body, options=options)
