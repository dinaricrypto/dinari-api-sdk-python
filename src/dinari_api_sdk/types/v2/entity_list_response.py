# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .entity import Entity
from ..._models import BaseModel

__all__ = ["EntityListResponse", "PaginatedEntityResponse", "PaginatedEntityResponsePaginationMetadata"]


class PaginatedEntityResponsePaginationMetadata(BaseModel):
    """Pagination metadata"""

    next: Optional[str] = None
    """Cursor for next page"""

    previous: Optional[str] = None
    """Cursor for previous page"""


class PaginatedEntityResponse(BaseModel):
    data: List[Entity]
    """List of Entity"""

    pagination_metadata: PaginatedEntityResponsePaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedEntityResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""


EntityListResponse: TypeAlias = Union[List[Entity], PaginatedEntityResponse]
