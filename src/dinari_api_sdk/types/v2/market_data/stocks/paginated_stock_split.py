# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from .stock_split import StockSplit
from ..pagination_metadata import PaginationMetadata

__all__ = ["PaginatedStockSplit"]


class PaginatedStockSplit(BaseModel):
    data: List[StockSplit]
    """List of StockSplit"""

    pagination_metadata: PaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedStockSplitResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""
