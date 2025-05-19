# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AccountRetrievePortfolioResponse", "Asset"]


class Asset(BaseModel):
    amount: float
    """Total amount of the dShare asset token in the `Account`."""

    chain_id: Literal["eip155:1", "eip155:42161", "eip155:8453", "eip155:81457", "eip155:7887", "eip155:98866"]
    """CAIP-2 chain ID of the blockchain where the dShare asset token exists."""

    stock_id: str
    """ID of the underlying `Stock` represented by the dShare asset token."""

    symbol: str
    """Token symbol of the dShare asset token."""

    token_address: str
    """Address of the dShare asset token."""


class AccountRetrievePortfolioResponse(BaseModel):
    assets: List[Asset]
    """Balance details for all owned `Stocks`."""
