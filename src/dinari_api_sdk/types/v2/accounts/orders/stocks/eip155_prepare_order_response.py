# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ......_models import BaseModel
from .order_fee_amount import OrderFeeAmount

__all__ = ["Eip155PrepareOrderResponse", "TransactionData"]


class TransactionData(BaseModel):
    """
    Information about a transaction to be signed with a wallet and submitted on chain.

    Typically the transactions will include an ERC20 approval transaction to allow the Dinari smart contract
    to spend the payment token or Dshare asset tokens on behalf of the user, followed by a transaction to call the Dinari smart contract to create an `Order`.
    """

    abi: object
    """
    [JSON ABI](https://docs.soliditylang.org/en/v0.8.30/abi-spec.html#json) of the
    smart contract function encoded in the transaction. Provided for informational
    purposes.
    """

    args: object
    """Arguments to the smart contract function encoded in the transaction.

    Provided for informational purposes.
    """

    contract_address: str
    """Smart contract address that the transaction should call."""

    data: str
    """Hex-encoded function call."""


class Eip155PrepareOrderResponse(BaseModel):
    """Prepared transactions to place an order on an EIP-155 (EVM) chain."""

    fees: List[OrderFeeAmount]
    """Fees included in the order transaction. Provided here as a reference."""

    transaction_data: List[TransactionData]
    """
    List of contract addresses and call data for building transactions to be signed
    and submitted on chain. Transactions should be submitted on chain in the order
    provided in this property.
    """
