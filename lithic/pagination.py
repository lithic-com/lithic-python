# File generated from our OpenAPI spec by Stainless.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import TypedDict

from pydantic import BaseModel

from ._types import ModelT
from ._base_client import BasePage, BaseSyncPage, BaseAsyncPage

__all__ = ["PageParams", "SyncPage", "AsyncPage"]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)


class PageParams(TypedDict, total=False):
    page: int
    """Page (for pagination)."""

    page_size: int
    """Page size (for pagination)."""


class SyncPage(BaseSyncPage[ModelT], BasePage[ModelT, PageParams], Generic[ModelT]):
    data: List[ModelT]
    page: int
    total_entries: int
    total_pages: int

    def _get_page_items(self) -> List[ModelT]:
        return self.data

    def next_page_params(self) -> Optional[PageParams]:
        current_page = self.page
        if not current_page < self.total_pages:
            return None
        return {"page": current_page + 1}


class AsyncPage(BaseAsyncPage[ModelT], BasePage[ModelT, PageParams], Generic[ModelT]):
    data: List[ModelT]
    page: int
    total_entries: int
    total_pages: int

    def _get_page_items(self) -> List[ModelT]:
        return self.data

    def next_page_params(self) -> Optional[PageParams]:
        current_page = self.page
        if not current_page < self.total_pages:
            return None
        return {"page": current_page + 1}
