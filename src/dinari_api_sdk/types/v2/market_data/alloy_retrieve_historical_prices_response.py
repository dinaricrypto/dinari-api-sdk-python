# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AlloyRetrieveHistoricalPricesResponse", "AlloyRetrieveHistoricalPricesResponseItem"]


class AlloyRetrieveHistoricalPricesResponseItem(BaseModel):
    """Datapoint of historical price data for an `Alloy`."""

    close: float
    """Close price from the given time period."""

    high: float
    """High price from the given time period."""

    low: float
    """Low price from the given time period."""

    open: float
    """Open price from the given time period."""

    timestamp: int
    """UNIX timestamp in seconds for the start of the aggregate window."""

    api_sv: Optional[Literal["AlloyHistoricalPriceDataPointV1:v1"]] = FieldInfo(alias="_sv", default=None)
    """Schema version"""


AlloyRetrieveHistoricalPricesResponse: TypeAlias = List[AlloyRetrieveHistoricalPricesResponseItem]
