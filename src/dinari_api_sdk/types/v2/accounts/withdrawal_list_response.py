# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .withdrawal import Withdrawal
from ..market_data.pagination_metadata import PaginationMetadata

__all__ = ["WithdrawalListResponse"]


class WithdrawalListResponse(BaseModel):
    data: List[Withdrawal]
    """List of Withdrawal"""

    pagination_metadata: PaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedWithdrawalResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""
