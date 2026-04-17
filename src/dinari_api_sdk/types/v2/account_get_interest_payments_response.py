# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import date
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "AccountGetInterestPaymentsResponse",
    "UnionMember0",
    "PaginatedInterestPaymentResponse",
    "PaginatedInterestPaymentResponseData",
    "PaginatedInterestPaymentResponsePaginationMetadata",
]


class UnionMember0(BaseModel):
    """An object representing an interest payment from stablecoin holdings."""

    amount: float
    """Amount of interest paid."""

    currency: str
    """Currency in which the interest was paid (e.g. USD)."""

    payment_date: date
    """Date of interest payment in US Eastern time zone. ISO 8601 format, YYYY-MM-DD."""


class PaginatedInterestPaymentResponseData(BaseModel):
    """An object representing an interest payment from stablecoin holdings."""

    amount: float
    """Amount of interest paid."""

    currency: str
    """Currency in which the interest was paid (e.g. USD)."""

    payment_date: date
    """Date of interest payment in US Eastern time zone. ISO 8601 format, YYYY-MM-DD."""


class PaginatedInterestPaymentResponsePaginationMetadata(BaseModel):
    """Pagination metadata"""

    next: Optional[str] = None
    """Cursor for next page"""

    previous: Optional[str] = None
    """Cursor for previous page"""


class PaginatedInterestPaymentResponse(BaseModel):
    data: List[PaginatedInterestPaymentResponseData]
    """List of InterestPayment"""

    pagination_metadata: PaginatedInterestPaymentResponsePaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedInterestPaymentResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""


AccountGetInterestPaymentsResponse: TypeAlias = Union[List[UnionMember0], PaginatedInterestPaymentResponse]
