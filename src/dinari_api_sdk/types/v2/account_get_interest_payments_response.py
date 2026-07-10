# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .market_data.pagination_metadata import PaginationMetadata

__all__ = ["AccountGetInterestPaymentsResponse", "Data"]


class Data(BaseModel):
    """An object representing an interest payment from stablecoin holdings."""

    amount: float
    """Amount of interest paid."""

    currency: str
    """Currency in which the interest was paid (e.g. USD)."""

    payment_date: date
    """Date of interest payment in US Eastern time zone. ISO 8601 format, YYYY-MM-DD."""


class AccountGetInterestPaymentsResponse(BaseModel):
    data: List[Data]
    """List of InterestPayment"""

    pagination_metadata: PaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedInterestPaymentResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""
