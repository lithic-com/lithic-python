# File generated from our OpenAPI spec by Stainless.

from typing import Optional, TypeVar, List, Generic, Dict, Any
from typing_extensions import TypedDict
from ._models import GenericModel
from ._types import FinalRequestOptions, ModelT
from ._base_client import BasePage, BaseSyncPage, BaseAsyncPage

__all__ = ["PaginationParams", "SyncPage", "AsyncPage"]


class PaginationParams(TypedDict, total=False):
    page: int
    page_size: int


class Page(BasePage[ModelT, PaginationParams], Generic[ModelT]):
    data: List[ModelT]
    page: int
    total_pages: int
    total_entries: int

    def has_next_page(self) -> bool:
        return self.page < self.total_pages

    def _next_page_params(self) -> PaginationParams:
        return {"page": self.page + 1}

    def _get_page_items(self) -> List[ModelT]:
        return self.data


class SyncPage(Page[ModelT], BaseSyncPage[ModelT], Generic[ModelT]):
    pass


class AsyncPage(Page[ModelT], BaseAsyncPage[ModelT], Generic[ModelT]):
    pass
