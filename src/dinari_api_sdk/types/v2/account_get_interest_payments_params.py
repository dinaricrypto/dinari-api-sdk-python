# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AccountGetInterestPaymentsParams"]


class AccountGetInterestPaymentsParams(TypedDict, total=False):
    end_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """End date, exclusive, in US Eastern time zone. ISO 8601 format, YYYY-MM-DD."""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(format="iso8601")]]
    """Start date, inclusive, in US Eastern time zone. ISO 8601 format, YYYY-MM-DD."""

    limit: int
    """Number of results to return"""

    next: Optional[str]
    """Cursor for next page"""

    order: Literal["asc", "desc"]
    """Sort order"""

    page: int

    page_size: int

    previous: Optional[str]
    """Cursor for previous page"""
