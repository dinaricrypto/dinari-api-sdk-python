# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..market_data.pagination_metadata import PaginationMetadata

__all__ = ["AccountListResponse", "Data"]


class Data(BaseModel):
    """Information about an `Account` owned by an `Entity`."""

    id: str
    """Unique ID for the `Account`."""

    created_dt: datetime
    """Datetime when the `Account` was created. ISO 8601 timestamp."""

    entity_id: str
    """ID for the `Entity` that owns the `Account`."""

    is_active: bool
    """Indicates whether the `Account` is active."""

    jurisdiction: Literal["BASELINE", "US"]
    """Jurisdiction of the `Account`."""

    brokerage_account_id: Optional[str] = None
    """ID of the brokerage account associated with the `Account`."""


class AccountListResponse(BaseModel):
    data: List[Data]
    """List of Account"""

    pagination_metadata: PaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedAccountResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""
