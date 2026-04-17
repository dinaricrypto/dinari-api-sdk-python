# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from .stock_split import StockSplit

__all__ = ["SplitListForStockResponse", "PaginatedStockSplitResponse", "PaginatedStockSplitResponsePaginationMetadata"]


class PaginatedStockSplitResponsePaginationMetadata(BaseModel):
    """Pagination metadata"""

    next: Optional[str] = None
    """Cursor for next page"""

    previous: Optional[str] = None
    """Cursor for previous page"""


class PaginatedStockSplitResponse(BaseModel):
    data: List[StockSplit]
    """List of StockSplit"""

    pagination_metadata: PaginatedStockSplitResponsePaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedStockSplitResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""


SplitListForStockResponse: TypeAlias = Union[List[StockSplit], PaginatedStockSplitResponse]
