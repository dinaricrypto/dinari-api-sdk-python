# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AlloyListResponse", "Data", "PaginationMetadata"]


class Data(BaseModel):
    """Alloy details."""

    id: Optional[str] = None
    """Unique identifier of the Alloy asset"""

    is_tradable: bool
    """Indicates if tradable on Dinari platform"""

    name: str
    """Name of the Alloy"""

    symbol: str
    """Symbol of the Alloy"""

    api_sv: Optional[Literal["Alloy:v1"]] = FieldInfo(alias="_sv", default=None)
    """Schema version"""


class PaginationMetadata(BaseModel):
    """Pagination metadata"""

    next: Optional[str] = None
    """Cursor for next page"""

    previous: Optional[str] = None
    """Cursor for previous page"""


class AlloyListResponse(BaseModel):
    """Paginated response containing a list of Alloys."""

    data: List[Data]
    """List of Alloys"""

    pagination_metadata: PaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedAlloyResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Schema version"""
