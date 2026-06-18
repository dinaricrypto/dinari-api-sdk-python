# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .withdrawal import Withdrawal

__all__ = ["WithdrawalListResponse", "PaginationMetadata"]


class PaginationMetadata(BaseModel):
    """Pagination metadata"""

    next: Optional[str] = None
    """Cursor for next page"""

    previous: Optional[str] = None
    """Cursor for previous page"""


class WithdrawalListResponse(BaseModel):
    data: List[Withdrawal]
    """List of Withdrawal"""

    pagination_metadata: PaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedWithdrawalResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""
