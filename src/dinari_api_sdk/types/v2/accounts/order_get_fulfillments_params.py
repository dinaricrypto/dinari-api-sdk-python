# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["OrderGetFulfillmentsParams"]


class OrderGetFulfillmentsParams(TypedDict, total=False):
    account_id: Required[str]

    limit: int
    """Number of results to return"""

    next: Optional[str]
    """Cursor for next page"""

    order: Literal["asc", "desc"]
    """Sort order"""

    previous: Optional[str]
    """Cursor for previous page"""
