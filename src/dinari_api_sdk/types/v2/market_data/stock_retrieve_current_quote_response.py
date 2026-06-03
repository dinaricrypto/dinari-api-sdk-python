# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = ["StockRetrieveCurrentQuoteResponse", "StockQuoteResponseV1", "StockQuoteResponseV2"]


class StockQuoteResponseV1(BaseModel):
    """Stock Quote"""

    ask_price: float
    """The ask price. 0 if there is no active ask."""

    ask_size: float
    """The ask size in shares."""

    bid_price: float
    """The bid price. 0 if there is no active bid."""

    bid_size: float
    """The bid size in shares."""

    stock_id: str
    """ID of the `Stock`"""

    timestamp: datetime
    """When the `StockQuote` was generated."""

    api_sv: Optional[Literal["StockQuote:v1"]] = FieldInfo(alias="_sv", default=None)
    """Schema version"""


class StockQuoteResponseV2(BaseModel):
    """Stock Quote"""

    ask_price: float
    """The ask price. 0 if there is no active ask."""

    ask_size: float
    """The ask size in shares."""

    bid_price: float
    """The bid price. 0 if there is no active bid."""

    bid_size: float
    """The bid size in shares."""

    stock_id: str
    """ID of the `Stock`"""

    timestamp: datetime
    """When the `StockQuote` was generated."""

    api_sv: Optional[Literal["StockQuote:v2"]] = FieldInfo(alias="_sv", default=None)
    """Schema version"""

    ask_exchange: Optional[str] = None
    """The ask exchange."""

    bid_exchange: Optional[str] = None
    """The bid exchange."""


StockRetrieveCurrentQuoteResponse: TypeAlias = Annotated[
    Union[StockQuoteResponseV1, StockQuoteResponseV2], PropertyInfo(discriminator="api_sv")
]
