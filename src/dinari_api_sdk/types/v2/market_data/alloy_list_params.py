# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

from ...._types import SequenceNotStr

__all__ = ["AlloyListParams"]


class AlloyListParams(TypedDict, total=False):
    limit: int
    """Number of results to return"""

    next: Optional[str]
    """Cursor for next page"""

    order: Literal["asc", "desc"]
    """Sort order"""

    previous: Optional[str]
    """Cursor for previous page"""

    symbols: SequenceNotStr[str]
    """If set, this endpoint will return Alloys that match the symbols specified"""
