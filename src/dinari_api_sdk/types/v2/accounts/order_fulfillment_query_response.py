# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "OrderFulfillmentQueryResponse",
    "UnionMember0",
    "PaginatedAccountOrderFulfillmentResponse",
    "PaginatedAccountOrderFulfillmentResponseData",
    "PaginatedAccountOrderFulfillmentResponsePaginationMetadata",
]


class UnionMember0(BaseModel):
    """Information about a fulfillment of an `Order`.

    An order may be fulfilled in multiple transactions.
    """

    id: str
    """ID of the `OrderFulfillment`."""

    asset_token_filled: float
    """Amount of dShare asset token filled for `BUY` orders."""

    asset_token_spent: float
    """Amount of dShare asset token spent for `SELL` orders."""

    chain_id: str
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

    alloy_id: Optional[str] = None
    """The `Alloy` ID associated with the `Order`"""

    payment_token_fee: Optional[float] = None
    """Fee amount, in payment tokens."""

    stock_id: Optional[str] = None
    """The `Stock` ID associated with the `Order`"""


class PaginatedAccountOrderFulfillmentResponseData(BaseModel):
    """Information about a fulfillment of an `Order`.

    An order may be fulfilled in multiple transactions.
    """

    id: str
    """ID of the `OrderFulfillment`."""

    asset_token_filled: float
    """Amount of dShare asset token filled for `BUY` orders."""

    asset_token_spent: float
    """Amount of dShare asset token spent for `SELL` orders."""

    chain_id: str
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

    alloy_id: Optional[str] = None
    """The `Alloy` ID associated with the `Order`"""

    payment_token_fee: Optional[float] = None
    """Fee amount, in payment tokens."""

    stock_id: Optional[str] = None
    """The `Stock` ID associated with the `Order`"""


class PaginatedAccountOrderFulfillmentResponsePaginationMetadata(BaseModel):
    """Pagination metadata"""

    next: Optional[str] = None
    """Cursor for next page"""

    previous: Optional[str] = None
    """Cursor for previous page"""


class PaginatedAccountOrderFulfillmentResponse(BaseModel):
    data: List[PaginatedAccountOrderFulfillmentResponseData]
    """List of AccountOrderFulfillment"""

    pagination_metadata: PaginatedAccountOrderFulfillmentResponsePaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedAccountOrderFulfillmentResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""


OrderFulfillmentQueryResponse: TypeAlias = Union[List[UnionMember0], PaginatedAccountOrderFulfillmentResponse]
