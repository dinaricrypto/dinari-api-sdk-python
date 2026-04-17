# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .token_transfer import TokenTransfer

__all__ = [
    "TokenTransferListResponse",
    "PaginatedTokenTransferResponse",
    "PaginatedTokenTransferResponsePaginationMetadata",
]


class PaginatedTokenTransferResponsePaginationMetadata(BaseModel):
    """Pagination metadata"""

    next: Optional[str] = None
    """Cursor for next page"""

    previous: Optional[str] = None
    """Cursor for previous page"""


class PaginatedTokenTransferResponse(BaseModel):
    data: List[TokenTransfer]
    """List of TokenTransfer"""

    pagination_metadata: PaginatedTokenTransferResponsePaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedTokenTransferResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""


TokenTransferListResponse: TypeAlias = Union[List[TokenTransfer], PaginatedTokenTransferResponse]
