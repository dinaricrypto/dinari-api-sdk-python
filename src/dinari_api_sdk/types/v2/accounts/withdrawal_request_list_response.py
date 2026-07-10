# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..market_data.pagination_metadata import PaginationMetadata

__all__ = ["WithdrawalRequestListResponse", "Data"]


class Data(BaseModel):
    """
    Information for a withdrawal request of payment tokens from an `Account` backed by a Dinari-managed `Wallet`.
    """

    id: str
    """ID of the `WithdrawalRequest`."""

    account_id: str
    """ID of the `Account` of the `WithdrawalRequest`."""

    created_dt: datetime
    """Datetime at which the `WithdrawalRequest` was created. ISO 8601 timestamp."""

    payment_token_amount: float
    """Amount of USD+ payment tokens submitted for withdrawal."""

    recipient_account_id: str
    """ID of the `Account` that will receive USDC payment tokens from the `Withdrawal`.

    This `Account` must be connected to a non-managed `Wallet` and belong to the
    same `Entity`.
    """

    status: Literal["PENDING", "SUBMITTED", "ERROR", "CANCELLED"]
    """Status of the `WithdrawalRequest`"""

    updated_dt: datetime
    """Datetime at which the `WithdrawalRequest` was updated. ISO 8601 timestamp."""


class WithdrawalRequestListResponse(BaseModel):
    data: List[Data]
    """List of WithdrawalRequest"""

    pagination_metadata: PaginationMetadata
    """Pagination metadata"""

    api_sv: Optional[Literal["PaginatedWithdrawalRequestResponse:v1"]] = FieldInfo(alias="_sv", default=None)
    """Version"""
