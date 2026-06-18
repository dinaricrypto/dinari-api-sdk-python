# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["V2ListOrdersResponse", "Data", "PaginationMetadata"]


class Data(BaseModel):
    id: str
    """ID of the `Order`."""

    chain_id: str
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

    payment_token: str
    """The payment token (stablecoin) address."""

    status: Literal[
        "PENDING_SUBMIT",
        "PENDING_CANCEL",
        "PENDING_ESCROW",
        "PENDING_FILL",
        "ESCROWED",
        "SUBMITTED",
        "CANCELLED",
        "PARTIALLY_FILLED",
        "FILLED",
        "REJECTED",
        "REQUIRING_CONTACT",
        "ERROR",
    ]
    """Status of the `Order`."""

    stock_id: str
    """The `Stock` ID associated with the `Order`"""

    account_id: Optional[str] = None
    """Account ID the order was made for."""

    asset_token: Optional[str] = None
    """The dShare asset token address."""

    asset_token_quantity: Optional[float] = None
    """Total amount of assets involved."""

    cancel_transaction_hash: Optional[str] = None
    """Transaction hash for cancellation of `Order`, if the `Order` was cancelled."""

    client_order_id: Optional[str] = None
    """
    Customer-supplied unique identifier to map this `Order` to an order in the
    customer's systems.
    """

    entity_id: Optional[str] = None
    """Entity ID of the Order"""

    fee: Optional[float] = None
    """Fee amount associated with `Order`."""

    limit_price: Optional[float] = None
    """
    For limit `Orders`, the price per asset, specified in the `Stock`'s native
    currency (USD for US equities and ETFs).
    """

    order_request_id: Optional[str] = None
    """Order Request ID for the `Order`"""

    payment_token_quantity: Optional[float] = None
    """Total amount of payment involved."""


class PaginationMetadata(BaseModel):
    """Pagination metadata"""

    next: Optional[str] = None
    """Cursor for next page"""

    previous: Optional[str] = None
    """Cursor for previous page"""


class V2ListOrdersResponse(BaseModel):
    data: List[Data]
    """List of EntityOrder"""

    pagination_metadata: PaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedEntityOrderResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""
