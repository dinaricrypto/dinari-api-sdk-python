# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["TokenTransfer"]


class TokenTransfer(BaseModel):
    """Information about a token transfer between accounts."""

    id: str
    """ID of the token transfer."""

    chain_id: Literal[
        "eip155:1",
        "eip155:42161",
        "eip155:8453",
        "eip155:81457",
        "eip155:98866",
        "eip155:999",
        "eip155:43114",
        "eip155:11155111",
        "eip155:421614",
        "eip155:84532",
        "eip155:168587773",
        "eip155:98867",
        "eip155:998",
        "eip155:43113",
        "eip155:202110",
        "eip155:179205",
        "eip155:179202",
        "eip155:98865",
        "eip155:7887",
    ]
    """CAIP-2 chain ID of the blockchain that the transfer is made on."""

    created_dt: datetime
    """Datetime at which the transfer was created. ISO 8601 timestamp."""

    quantity: float
    """Quantity of the token being transferred."""

    recipient_account_id: str
    """ID of the account to which the tokens are transferred."""

    sender_account_id: str
    """ID of the account from which the tokens are transferred."""

    status: Literal["PENDING", "IN_PROGRESS", "COMPLETE", "FAILED"]
    """Status of the token transfer."""

    token_address: str
    """Address of the token being transferred."""

    updated_dt: datetime
    """Datetime at which the transfer was last updated. ISO 8601 timestamp."""

    transaction_hash: Optional[str] = None
    """Transaction hash of the transfer on the blockchain, if applicable.

    This is only present if the transfer has been executed on-chain.
    """
