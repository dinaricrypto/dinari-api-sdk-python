# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ExternalConnectParams"]


class ExternalConnectParams(TypedDict, total=False):
    chain_id: Required[
        Literal["eip155:1", "eip155:42161", "eip155:8453", "eip155:81457", "eip155:7887", "eip155:98866", "eip155:0"]
    ]
    """CAIP-2 formatted chain ID of the blockchain the `Wallet` to link is on.

    eip155:0 is used for EOA wallets
    """

    nonce: Required[str]
    """Nonce contained within the connection message."""

    signature: Required[str]
    """Signature payload from signing the connection message with the `Wallet`."""

    wallet_address: Required[str]
    """Address of the `Wallet`."""
