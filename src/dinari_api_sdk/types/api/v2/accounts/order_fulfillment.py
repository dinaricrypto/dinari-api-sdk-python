# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["OrderFulfillment"]


class OrderFulfillment(BaseModel):
    id: str
    """ID of the `OrderFulfillment`."""

    asset_token_filled: float
    """Amount of dShare asset token filled for `BUY` orders."""

    asset_token_spent: float
    """Amount of dShare asset token spent for `SELL` orders."""

    chain_id: Literal["eip155:1", "eip155:42161", "eip155:8453", "eip155:81457", "eip155:7887", "eip155:98866"]
    """Blockchain that the transaction was run on."""

    order_id: str
    """ID of the `Order` this `OrderFulfillment` is for."""

    payment_token_filled: float
    """Amount of payment token filled for `SELL` orders."""

    payment_token_spent: float
    """Amount of payment token spent for `BUY` orders."""

    transaction_dt: datetime
    """Time when transaction occurred."""

    transaction_hash: str
    """Transaction hash for this fulfillment."""

    payment_token_fee: Optional[float] = None
    """Fee amount, in payment tokens."""
