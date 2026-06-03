# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["StockRetrieveCurrentQuoteParams"]


class StockRetrieveCurrentQuoteParams(TypedDict, total=False):
    feed: Optional[Literal["sip"]]
    """Requested data source for the quote.

    Only applies when using x-api-version: 2. Allowed values:

    - `null`: (default) Selects the highest quality available free data source.
    - `sip`: Consolidated quote from all U.S. exchanges (NBBO). This is a paid data
      source and incurs usage-based billing.
    """

    x_api_version: Annotated[str, PropertyInfo(alias="X-API-Version")]
