# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .entity import Entity
from ..._models import BaseModel

__all__ = ["EntityListResponse", "PaginationMetadata"]


class PaginationMetadata(BaseModel):
    """Pagination metadata"""

    next: Optional[str] = None
    """Cursor for next page"""

    previous: Optional[str] = None
    """Cursor for previous page"""


class EntityListResponse(BaseModel):
    data: List[Entity]
    """List of Entity"""

    pagination_metadata: PaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedEntityResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""
