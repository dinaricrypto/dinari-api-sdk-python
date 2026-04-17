# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, TypedDict

__all__ = ["OrderListParams"]


class OrderListParams(TypedDict, total=False):
    chain_id: Optional[str]
    """CAIP-2 formatted chain ID of the blockchain the `Order` was made on."""

    client_order_id: Optional[str]
    """Customer-supplied identifier to search for `Order`s."""

    limit: int
    """Number of results to return"""

    next: Optional[str]
    """Cursor for next page"""

    order: Literal["asc", "desc"]
    """Sort order"""

    order_transaction_hash: Optional[str]
    """Transaction hash of the `Order`."""

    page: int

    page_size: int

    previous: Optional[str]
    """Cursor for previous page"""
