# File generated from our OpenAPI spec by Stainless.

from typing import List, Generic, TypeVar, Optional

from ._types import ModelT
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncPage", "AsyncPage"]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)


class SyncPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    data: List[ModelT]
    page: int
    total_entries: int
    total_pages: int

    def _get_page_items(self) -> List[ModelT]:
        return self.data

    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page
        if not current_page < self.total_pages:
            return None
        return PageInfo(params={"page": current_page + 1})


class AsyncPage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    data: List[ModelT]
    page: int
    total_entries: int
    total_pages: int

    def _get_page_items(self) -> List[ModelT]:
        return self.data

    def next_page_info(self) -> Optional[PageInfo]:
        current_page = self.page
        if not current_page < self.total_pages:
            return None
        return PageInfo(params={"page": current_page + 1})
