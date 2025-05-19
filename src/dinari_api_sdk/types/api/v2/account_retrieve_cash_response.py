# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = ["AccountRetrieveCashResponse", "AccountRetrieveCashResponseItem"]


class AccountRetrieveCashResponseItem(BaseModel):
    amount: float
    """Total amount of the payment token in the `Account`."""

    chain_id: Literal["eip155:1", "eip155:42161", "eip155:8453", "eip155:81457", "eip155:7887", "eip155:98866"]
    """CAIP-2 chain ID of the payment token."""

    symbol: str
    """Symbol of the payment token."""

    token_address: str
    """Address of the payment token."""


AccountRetrieveCashResponse: TypeAlias = List[AccountRetrieveCashResponseItem]
