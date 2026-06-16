# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["OrderRequestCreateLimitBuyParams"]


class OrderRequestCreateLimitBuyParams(TypedDict, total=False):
    asset_quantity: Required[float]
    """Amount of dShare asset involved.

    Required for limit `Order Requests` and market sell `Order Requests`. Must be a
    positive number with a precision of up to 4 decimal places.
    """

    limit_price: Required[float]
    """Price at which to execute the order.

    Must be a positive number with a precision of up to 2 decimal places.
    """

    alloy_id: Optional[str]
    """ID of `Alloy`."""

    client_order_id: Optional[str]
    """Customer-supplied ID to map this order to an order in their own systems.

    Must be unique within the entity.
    """

    fee: Optional[float]
    """Optional fee amount associated with `Order` in USD for DFN orders.

    Must be a positive number with a precision of up to 6 decimal places.
    """

    payment_token_address: Optional[str]
    """Address of the payment token to be used for the payment of the order.

    If not provided, the default payment token (USD+) will be used.
    """

    recipient_account_id: Optional[str]
    """ID of `Account` to receive the `Order`."""

    stock_id: Optional[str]
    """ID of `Stock`."""
