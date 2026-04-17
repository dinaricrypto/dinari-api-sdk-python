# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .withdrawal import Withdrawal

__all__ = ["WithdrawalListResponse", "PaginatedWithdrawalResponse", "PaginatedWithdrawalResponsePaginationMetadata"]


class PaginatedWithdrawalResponsePaginationMetadata(BaseModel):
    """Pagination metadata"""

    next: Optional[str] = None
    """Cursor for next page"""

    previous: Optional[str] = None
    """Cursor for previous page"""


class PaginatedWithdrawalResponse(BaseModel):
    data: List[Withdrawal]
    """List of Withdrawal"""

    pagination_metadata: PaginatedWithdrawalResponsePaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedWithdrawalResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""


WithdrawalListResponse: TypeAlias = Union[List[Withdrawal], PaginatedWithdrawalResponse]
