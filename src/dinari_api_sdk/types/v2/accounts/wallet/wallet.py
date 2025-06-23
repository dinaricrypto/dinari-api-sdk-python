# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["Wallet"]


class Wallet(BaseModel):
    address: str
    """Address of the `Wallet`."""

    chain_id: Literal[
        "eip155:1", "eip155:42161", "eip155:8453", "eip155:81457", "eip155:7887", "eip155:98866", "eip155:0"
    ]
    """CAIP-2 formatted chain ID of the blockchain the `Wallet` is on.

    eip155:0 is used for EOA wallets
    """

    is_aml_flagged: bool
    """Indicates whether the `Wallet` is flagged for AML violation."""

    is_managed_wallet: bool
    """Indicates whether the `Wallet` is a Dinari-managed wallet."""
