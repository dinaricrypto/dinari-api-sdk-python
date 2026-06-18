# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from ...._types import SequenceNotStr

__all__ = ["StockListParams"]


class StockListParams(TypedDict, total=False):
    limit: int
    """Number of results to return"""

    next: Optional[str]
    """Cursor for next page"""

    order: Literal["asc", "desc"]
    """Sort order"""

    previous: Optional[str]
    """Cursor for previous page"""

    symbols: SequenceNotStr[str]
    """List of `Stock` symbols to query. If not provided, all `Stocks` are returned."""
