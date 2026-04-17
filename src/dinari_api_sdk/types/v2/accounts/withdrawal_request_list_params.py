# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["WithdrawalRequestListParams"]


class WithdrawalRequestListParams(TypedDict, total=False):
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
