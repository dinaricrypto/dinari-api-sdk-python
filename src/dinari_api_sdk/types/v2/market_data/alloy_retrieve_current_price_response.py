# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AlloyRetrieveCurrentPriceResponse"]


class AlloyRetrieveCurrentPriceResponse(BaseModel):
    id: str
    """ID of the `Alloy` asset."""

    price: float
    """Current trade price."""

    timestamp: datetime
    """When the price was generated."""

    api_sv: Optional[Literal["AlloyPrice:v1"]] = FieldInfo(alias="_sv", default=None)
    """Schema version"""
