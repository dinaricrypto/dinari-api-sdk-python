# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["OrderRequest"]


class OrderRequest(BaseModel):
    id: str
    """ID of `OrderRequest`.

    This is the primary identifier for the `/order_requests` routes.
    """

    account_id: str
    """ID of `Account` placing the `OrderRequest`."""

    created_dt: datetime
    """Datetime at which the `OrderRequest` was created. ISO 8601 timestamp."""

    order_side: Literal["BUY", "SELL"]
    """Indicates whether `Order` is a buy or sell."""

    order_tif: Literal["DAY", "GTC", "IOC", "FOK"]
    """Indicates how long `Order` is valid for."""

    order_type: Literal["MARKET", "LIMIT"]
    """Type of `Order`."""

    status: Literal["PENDING", "SUBMITTED", "ERROR", "CANCELLED"]
    """Status of `OrderRequest`."""

    order_id: Optional[str] = None
    """ID of `Order` created from the `OrderRequest`.

    This is the primary identifier for the `/orders` routes.
    """
