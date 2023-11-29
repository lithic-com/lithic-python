# File generated from our OpenAPI spec by Stainless.

from typing import Any, List, Generic, TypeVar, Optional, cast
from typing_extensions import Protocol, override, runtime_checkable

from ._types import ModelT
from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncCursorPage", "AsyncCursorPage", "SyncSinglePage", "AsyncSinglePage"]

_BaseModelT = TypeVar("_BaseModelT", bound=BaseModel)


@runtime_checkable
class CursorPageItem(Protocol):
    token: Optional[str]


class SyncCursorPage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    data: List[ModelT]
    has_more: bool

    @override
    def _get_page_items(self) -> List[ModelT]:
        data = self.data
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("ending_before", False)

        if not self.data:
            return None

        if is_forwards:
            item = cast(Any, self.data[-1])
            if not isinstance(item, CursorPageItem) or item.token is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"starting_after": item.token})
        else:
            item = cast(Any, self.data[0])
            if not isinstance(item, CursorPageItem) or item.token is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"ending_before": item.token})


class AsyncCursorPage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    data: List[ModelT]
    has_more: bool

    @override
    def _get_page_items(self) -> List[ModelT]:
        data = self.data
        return data

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        is_forwards = not self._options.params.get("ending_before", False)

        if not self.data:
            return None

        if is_forwards:
            item = cast(Any, self.data[-1])
            if not isinstance(item, CursorPageItem) or item.token is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"starting_after": item.token})
        else:
            item = cast(Any, self.data[0])
            if not isinstance(item, CursorPageItem) or item.token is None:
                # TODO emit warning log
                return None

            return PageInfo(params={"ending_before": item.token})


class SyncSinglePage(BaseSyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    data: List[ModelT]
    has_more: bool

    @override
    def _get_page_items(self) -> List[ModelT]:
        data = self.data
        return data

    @override
    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None


class AsyncSinglePage(BaseAsyncPage[ModelT], BasePage[ModelT], Generic[ModelT]):
    data: List[ModelT]
    has_more: bool

    @override
    def _get_page_items(self) -> List[ModelT]:
        data = self.data
        return data

    @override
    def next_page_info(self) -> None:
        """
        This page represents a response that isn't actually paginated at the API level
        so there will never be a next page.
        """
        return None
