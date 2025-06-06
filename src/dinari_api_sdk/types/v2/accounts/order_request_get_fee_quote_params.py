# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .order_side import OrderSide
from .order_type import OrderType

__all__ = ["OrderRequestGetFeeQuoteParams"]


class OrderRequestGetFeeQuoteParams(TypedDict, total=False):
    order_side: Required[OrderSide]
    """Indicates whether `Order Request` is a buy or sell."""

    order_type: Required[OrderType]
    """Type of `Order Request`."""

    stock_id: Required[str]
    """The Stock ID associated with the Order Request"""

    asset_token_quantity: float
    """Amount of dShare asset tokens involved.

    Required for limit `Orders` and market sell `Order Requests`.
    """

    limit_price: float
    """Price per asset in the asset's native currency.

    USD for US equities and ETFs. Required for limit `Order Requests`.
    """

    payment_token_quantity: float
    """Amount of payment tokens involved. Required for market buy `Order Requests`."""
