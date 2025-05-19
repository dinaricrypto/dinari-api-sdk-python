# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["Order"]


class Order(BaseModel):
    id: str
    """ID of the `Order`."""

    chain_id: Literal["eip155:1", "eip155:42161", "eip155:8453", "eip155:81457", "eip155:7887", "eip155:98866"]
    """
    CAIP-2 formatted chain ID of the blockchain that the `Order` transaction was run
    on.
    """

    created_dt: datetime
    """Datetime at which the `Order` was created. ISO 8601 timestamp."""

    order_contract_address: str
    """Smart contract address that `Order` was created from."""

    order_side: Literal["BUY", "SELL"]
    """Indicates whether `Order` is a buy or sell."""

    order_tif: Literal["DAY", "GTC", "IOC", "FOK"]
    """Time in force. Indicates how long `Order` is valid for."""

    order_transaction_hash: str
    """Transaction hash for the `Order` creation."""

    order_type: Literal["MARKET", "LIMIT"]
    """Type of `Order`."""

    status: Literal[
        "PENDING_SUBMIT",
        "PENDING_CANCEL",
        "PENDING_ESCROW",
        "PENDING_FILL",
        "ESCROWED",
        "SUBMITTED",
        "CANCELLED",
        "FILLED",
        "REJECTED",
        "REQUIRING_CONTACT",
        "ERROR",
    ]
    """Status of the `Order`."""

    stock_id: str
    """The `Stock` ID associated with the `Order`"""

    asset_token: Optional[str] = None
    """The dShare asset token address."""

    asset_token_quantity: Optional[float] = None
    """Total amount of assets involved."""

    cancel_transaction_hash: Optional[str] = None
    """Transaction hash for cancellation of `Order`, if the `Order` was cancelled."""

    fee: Optional[float] = None
    """Fee amount associated with `Order`."""

    limit_price: Optional[float] = None
    """
    For limit `Orders`, the price per asset, specified in the `Stock`'s native
    currency (USD for US equities and ETFs).
    """

    payment_token: Optional[str] = None
    """The payment token (stablecoin) address."""

    payment_token_quantity: Optional[float] = None
    """Total amount of payment involved."""
