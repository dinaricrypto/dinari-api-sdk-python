# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .token_transfer import TokenTransfer

__all__ = ["TokenTransferListResponse", "PaginationMetadata"]


class PaginationMetadata(BaseModel):
    """Pagination metadata"""

    next: Optional[str] = None
    """Cursor for next page"""

    previous: Optional[str] = None
    """Cursor for previous page"""


class TokenTransferListResponse(BaseModel):
    data: List[TokenTransfer]
    """List of TokenTransfer"""

    pagination_metadata: PaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedTokenTransferResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""
