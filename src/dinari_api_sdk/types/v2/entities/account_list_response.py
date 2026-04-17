# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .account import Account
from ...._models import BaseModel

__all__ = ["AccountListResponse", "PaginatedAccountResponse", "PaginatedAccountResponsePaginationMetadata"]


class PaginatedAccountResponsePaginationMetadata(BaseModel):
    """Pagination metadata"""

    next: Optional[str] = None
    """Cursor for next page"""

    previous: Optional[str] = None
    """Cursor for previous page"""


class PaginatedAccountResponse(BaseModel):
    data: List[Account]
    """List of Account"""

    pagination_metadata: PaginatedAccountResponsePaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedAccountResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""


AccountListResponse: TypeAlias = Union[List[Account], PaginatedAccountResponse]
