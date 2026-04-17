# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .withdrawal_request import WithdrawalRequest

__all__ = [
    "WithdrawalRequestListResponse",
    "PaginatedWithdrawalRequestResponse",
    "PaginatedWithdrawalRequestResponsePaginationMetadata",
]


class PaginatedWithdrawalRequestResponsePaginationMetadata(BaseModel):
    """Pagination metadata"""

    next: Optional[str] = None
    """Cursor for next page"""

    previous: Optional[str] = None
    """Cursor for previous page"""


class PaginatedWithdrawalRequestResponse(BaseModel):
    data: List[WithdrawalRequest]
    """List of WithdrawalRequest"""

    pagination_metadata: PaginatedWithdrawalRequestResponsePaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedWithdrawalRequestResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""


WithdrawalRequestListResponse: TypeAlias = Union[List[WithdrawalRequest], PaginatedWithdrawalRequestResponse]
