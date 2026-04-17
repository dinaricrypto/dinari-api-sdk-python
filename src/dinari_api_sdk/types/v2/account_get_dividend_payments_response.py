# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import date
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "AccountGetDividendPaymentsResponse",
    "UnionMember0",
    "PaginatedDividendPaymentResponse",
    "PaginatedDividendPaymentResponseData",
    "PaginatedDividendPaymentResponsePaginationMetadata",
]


class UnionMember0(BaseModel):
    """Represents a dividend payment event for an `Account`."""

    amount: float
    """Amount of the dividend paid."""

    currency: str
    """Currency in which the dividend was paid. (e.g. USD)"""

    payment_date: date
    """Date the dividend was distributed to the account. ISO 8601 format, YYYY-MM-DD."""

    stock_id: str
    """ID of the `Stock` for which the dividend was paid."""


class PaginatedDividendPaymentResponseData(BaseModel):
    """Represents a dividend payment event for an `Account`."""

    amount: float
    """Amount of the dividend paid."""

    currency: str
    """Currency in which the dividend was paid. (e.g. USD)"""

    payment_date: date
    """Date the dividend was distributed to the account. ISO 8601 format, YYYY-MM-DD."""

    stock_id: str
    """ID of the `Stock` for which the dividend was paid."""


class PaginatedDividendPaymentResponsePaginationMetadata(BaseModel):
    """Pagination metadata"""

    next: Optional[str] = None
    """Cursor for next page"""

    previous: Optional[str] = None
    """Cursor for previous page"""


class PaginatedDividendPaymentResponse(BaseModel):
    data: List[PaginatedDividendPaymentResponseData]
    """List of DividendPayment"""

    pagination_metadata: PaginatedDividendPaymentResponsePaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedDividendPaymentResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""


AccountGetDividendPaymentsResponse: TypeAlias = Union[List[UnionMember0], PaginatedDividendPaymentResponse]
