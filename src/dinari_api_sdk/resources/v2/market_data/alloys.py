# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.v2.market_data import alloy_list_params, alloy_retrieve_historical_prices_params
from ....types.v2.market_data.alloy_list_response import AlloyListResponse
from ....types.v2.market_data.alloy_retrieve_current_price_response import AlloyRetrieveCurrentPriceResponse
from ....types.v2.market_data.alloy_retrieve_historical_prices_response import AlloyRetrieveHistoricalPricesResponse

__all__ = ["AlloysResource", "AsyncAlloysResource"]


class AlloysResource(SyncAPIResource):
    """
    **Dinari provides basic market data for `Stocks` and `Alloys` that are available to transact on.**

    This data is provided on a best-effort basis and we recommend using a dedicated provider for more intensive market data needs.
    """

    @cached_property
    def with_raw_response(self) -> AlloysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dinaricrypto/dinari-api-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AlloysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AlloysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dinaricrypto/dinari-api-sdk-python#with_streaming_response
        """
        return AlloysResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        next: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        previous: Optional[str] | Omit = omit,
        symbols: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlloyListResponse:
        """
        Returns available `Alloys` with cursor-based pagination.

        Args:
          limit: Number of results to return

          next: Cursor for next page

          order: Sort order

          previous: Cursor for previous page

          symbols: If set, this endpoint will return Alloys that match the symbols specified

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/v2/market_data/alloys/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "next": next,
                        "order": order,
                        "previous": previous,
                        "symbols": symbols,
                    },
                    alloy_list_params.AlloyListParams,
                ),
            ),
            cast_to=AlloyListResponse,
        )

    def retrieve_current_price(
        self,
        alloy_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlloyRetrieveCurrentPriceResponse:
        """
        Get the current price for a specified `Alloy`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alloy_id:
            raise ValueError(f"Expected a non-empty value for `alloy_id` but received {alloy_id!r}")
        return self._get(
            path_template("/api/v2/market_data/alloys/{alloy_id}/current_price", alloy_id=alloy_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlloyRetrieveCurrentPriceResponse,
        )

    def retrieve_historical_prices(
        self,
        alloy_id: str,
        *,
        timespan: Literal["DAY", "WEEK"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlloyRetrieveHistoricalPricesResponse:
        """Get historical price data for a specified `Alloy`.

        Each index in the array
        represents a single tick in a price chart.

        Args:
          timespan: The timespan of the historical prices to query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alloy_id:
            raise ValueError(f"Expected a non-empty value for `alloy_id` but received {alloy_id!r}")
        return self._get(
            path_template("/api/v2/market_data/alloys/{alloy_id}/historical_prices/", alloy_id=alloy_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"timespan": timespan}, alloy_retrieve_historical_prices_params.AlloyRetrieveHistoricalPricesParams
                ),
            ),
            cast_to=AlloyRetrieveHistoricalPricesResponse,
        )


class AsyncAlloysResource(AsyncAPIResource):
    """
    **Dinari provides basic market data for `Stocks` and `Alloys` that are available to transact on.**

    This data is provided on a best-effort basis and we recommend using a dedicated provider for more intensive market data needs.
    """

    @cached_property
    def with_raw_response(self) -> AsyncAlloysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dinaricrypto/dinari-api-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAlloysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAlloysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dinaricrypto/dinari-api-sdk-python#with_streaming_response
        """
        return AsyncAlloysResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        next: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        previous: Optional[str] | Omit = omit,
        symbols: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlloyListResponse:
        """
        Returns available `Alloys` with cursor-based pagination.

        Args:
          limit: Number of results to return

          next: Cursor for next page

          order: Sort order

          previous: Cursor for previous page

          symbols: If set, this endpoint will return Alloys that match the symbols specified

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/v2/market_data/alloys/",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "next": next,
                        "order": order,
                        "previous": previous,
                        "symbols": symbols,
                    },
                    alloy_list_params.AlloyListParams,
                ),
            ),
            cast_to=AlloyListResponse,
        )

    async def retrieve_current_price(
        self,
        alloy_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlloyRetrieveCurrentPriceResponse:
        """
        Get the current price for a specified `Alloy`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alloy_id:
            raise ValueError(f"Expected a non-empty value for `alloy_id` but received {alloy_id!r}")
        return await self._get(
            path_template("/api/v2/market_data/alloys/{alloy_id}/current_price", alloy_id=alloy_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AlloyRetrieveCurrentPriceResponse,
        )

    async def retrieve_historical_prices(
        self,
        alloy_id: str,
        *,
        timespan: Literal["DAY", "WEEK"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AlloyRetrieveHistoricalPricesResponse:
        """Get historical price data for a specified `Alloy`.

        Each index in the array
        represents a single tick in a price chart.

        Args:
          timespan: The timespan of the historical prices to query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not alloy_id:
            raise ValueError(f"Expected a non-empty value for `alloy_id` but received {alloy_id!r}")
        return await self._get(
            path_template("/api/v2/market_data/alloys/{alloy_id}/historical_prices/", alloy_id=alloy_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"timespan": timespan}, alloy_retrieve_historical_prices_params.AlloyRetrieveHistoricalPricesParams
                ),
            ),
            cast_to=AlloyRetrieveHistoricalPricesResponse,
        )


class AlloysResourceWithRawResponse:
    def __init__(self, alloys: AlloysResource) -> None:
        self._alloys = alloys

        self.list = to_raw_response_wrapper(
            alloys.list,
        )
        self.retrieve_current_price = to_raw_response_wrapper(
            alloys.retrieve_current_price,
        )
        self.retrieve_historical_prices = to_raw_response_wrapper(
            alloys.retrieve_historical_prices,
        )


class AsyncAlloysResourceWithRawResponse:
    def __init__(self, alloys: AsyncAlloysResource) -> None:
        self._alloys = alloys

        self.list = async_to_raw_response_wrapper(
            alloys.list,
        )
        self.retrieve_current_price = async_to_raw_response_wrapper(
            alloys.retrieve_current_price,
        )
        self.retrieve_historical_prices = async_to_raw_response_wrapper(
            alloys.retrieve_historical_prices,
        )


class AlloysResourceWithStreamingResponse:
    def __init__(self, alloys: AlloysResource) -> None:
        self._alloys = alloys

        self.list = to_streamed_response_wrapper(
            alloys.list,
        )
        self.retrieve_current_price = to_streamed_response_wrapper(
            alloys.retrieve_current_price,
        )
        self.retrieve_historical_prices = to_streamed_response_wrapper(
            alloys.retrieve_historical_prices,
        )


class AsyncAlloysResourceWithStreamingResponse:
    def __init__(self, alloys: AsyncAlloysResource) -> None:
        self._alloys = alloys

        self.list = async_to_streamed_response_wrapper(
            alloys.list,
        )
        self.retrieve_current_price = async_to_streamed_response_wrapper(
            alloys.retrieve_current_price,
        )
        self.retrieve_historical_prices = async_to_streamed_response_wrapper(
            alloys.retrieve_historical_prices,
        )
