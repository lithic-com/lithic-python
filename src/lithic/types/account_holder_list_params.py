# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AccountHolderListParams"]


class AccountHolderListParams(TypedDict, total=False):
    begin: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created after the specified time will be included. UTC time zone.
    """

    email: str
    """Email address of the account holder.

    The query must be an exact match, case insensitive.
    """

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Date string in RFC 3339 format.

    Only entries created before the specified time will be included. UTC time zone.
    """

    ending_before: str
    """A cursor representing an item's token before which a page of results should end.

    Used to retrieve the previous page of results before this item.
    """

    external_id: str
    """If applicable, represents the external_id associated with the account_holder."""

    first_name: str
    """(Individual Account Holders only) The first name of the account holder.

    The query is case insensitive and supports partial matches.
    """

    last_name: str
    """(Individual Account Holders only) The last name of the account holder.

    The query is case insensitive and supports partial matches.
    """

    legal_business_name: str
    """(Business Account Holders only) The legal business name of the account holder.

    The query is case insensitive and supports partial matches.
    """

    limit: int
    """The number of account_holders to limit the response to."""

    phone_number: str
    """Phone number of the account holder. The query must be an exact match."""

    starting_after: str
    """A cursor representing an item's token after which a page of results should
    begin.

    Used to retrieve the next page of results after this item.
    """
