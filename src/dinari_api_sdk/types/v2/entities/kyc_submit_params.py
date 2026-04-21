# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .us_kyc_check_data_param import UsKYCCheckDataParam
from .baseline_kyc_check_data_param import BaselineKYCCheckDataParam

__all__ = ["KYCSubmitParams", "CreateBaselineKYCInput", "CreateUsKYCInput"]


class CreateBaselineKYCInput(TypedDict, total=False):
    data: Required[BaselineKYCCheckDataParam]
    """KYC data of the `Entity`."""

    provider_name: Required[str]
    """Name of the KYC provider that provided the KYC information."""

    jurisdiction: Literal["BASELINE"]
    """Jurisdiction of the KYC check."""


class CreateUsKYCInput(TypedDict, total=False):
    data: Required[UsKYCCheckDataParam]
    """KYC data of the `Entity`."""

    provider_name: Required[str]
    """Name of the KYC provider that provided the KYC information."""

    jurisdiction: Literal["US"]
    """Jurisdiction of the KYC check."""


KYCSubmitParams: TypeAlias = Union[CreateBaselineKYCInput, CreateUsKYCInput]
