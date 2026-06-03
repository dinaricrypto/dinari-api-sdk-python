# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
from typing_extensions import Literal

import httpx

from .splits import (
    SplitsResource,
    AsyncSplitsResource,
    SplitsResourceWithRawResponse,
    AsyncSplitsResourceWithRawResponse,
    SplitsResourceWithStreamingResponse,
    AsyncSplitsResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ....._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.v2.market_data import (
    stock_list_params,
    stock_retrieve_news_params,
    stock_retrieve_current_quote_params,
    stock_retrieve_historical_prices_params,
)
from .....types.v2.market_data.stock_list_response import StockListResponse
from .....types.v2.market_data.stock_retrieve_news_response import StockRetrieveNewsResponse
from .....types.v2.market_data.stock_retrieve_dividends_response import StockRetrieveDividendsResponse
from .....types.v2.market_data.stock_retrieve_current_price_response import StockRetrieveCurrentPriceResponse
from .....types.v2.market_data.stock_retrieve_current_quote_response import StockRetrieveCurrentQuoteResponse
from .....types.v2.market_data.stock_retrieve_historical_prices_response import StockRetrieveHistoricalPricesResponse

__all__ = ["StocksResource", "AsyncStocksResource"]


class StocksResource(SyncAPIResource):
    @cached_property
    def splits(self) -> SplitsResource:
        """**Corporate actions are events that affect the ownership of a `Stock`.**

        Corporate actions include dividends and stock splits.
        """
        return SplitsResource(self._client)

    @cached_property
    def with_raw_response(self) -> StocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dinaricrypto/dinari-api-sdk-python#accessing-raw-response-data-eg-headers
        """
        return StocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dinaricrypto/dinari-api-sdk-python#with_streaming_response
        """
        return StocksResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        limit: int | Omit = omit,
        next: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        previous: Optional[str] | Omit = omit,
        symbols: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockListResponse:
        """
        Get a list of `Stocks`.

        Args:
          limit: Number of results to return

          next: Cursor for next page

          order: Sort order

          previous: Cursor for previous page

          symbols: List of `Stock` symbols to query. If not provided, all `Stocks` are returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            StockListResponse,
            self._get(
                "/api/v2/market_data/stocks/",
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
                            "page": page,
                            "page_size": page_size,
                            "previous": previous,
                            "symbols": symbols,
                        },
                        stock_list_params.StockListParams,
                    ),
                ),
                cast_to=cast(Any, StockListResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve_current_price(
        self,
        stock_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockRetrieveCurrentPriceResponse:
        """
        Get current price for a specified `Stock`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stock_id:
            raise ValueError(f"Expected a non-empty value for `stock_id` but received {stock_id!r}")
        return self._get(
            path_template("/api/v2/market_data/stocks/{stock_id}/current_price", stock_id=stock_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StockRetrieveCurrentPriceResponse,
        )

    def retrieve_current_quote(
        self,
        stock_id: str,
        *,
        feed: Optional[Literal["sip"]] | Omit = omit,
        x_api_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockRetrieveCurrentQuoteResponse:
        """
        Get quote for a specified `Stock`.

        Args:
          feed: Requested data source for the quote. Only applies when using x-api-version: 2.
              Allowed values:

              - `null`: (default) Selects the highest quality available free data source.
              - `sip`: Consolidated quote from all U.S. exchanges (NBBO). This is a paid data
                source and incurs usage-based billing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stock_id:
            raise ValueError(f"Expected a non-empty value for `stock_id` but received {stock_id!r}")
        extra_headers = {**strip_not_given({"X-API-Version": x_api_version}), **(extra_headers or {})}
        return cast(
            StockRetrieveCurrentQuoteResponse,
            self._get(
                path_template("/api/v2/market_data/stocks/{stock_id}/current_quote", stock_id=stock_id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {"feed": feed}, stock_retrieve_current_quote_params.StockRetrieveCurrentQuoteParams
                    ),
                ),
                cast_to=cast(
                    Any, StockRetrieveCurrentQuoteResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def retrieve_dividends(
        self,
        stock_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockRetrieveDividendsResponse:
        """
        Get a list of announced stock dividend details for a specified `Stock`.

        Note that this data applies only to actual stocks. Yield received for holding
        tokenized shares may differ from this.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stock_id:
            raise ValueError(f"Expected a non-empty value for `stock_id` but received {stock_id!r}")
        return self._get(
            path_template("/api/v2/market_data/stocks/{stock_id}/dividends", stock_id=stock_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StockRetrieveDividendsResponse,
        )

    def retrieve_historical_prices(
        self,
        stock_id: str,
        *,
        timespan: Literal["DAY", "WEEK", "MONTH", "YEAR"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockRetrieveHistoricalPricesResponse:
        """Get historical price data for a specified `Stock`.

        Each index in the array
        represents a single tick in a price chart.

        Args:
          timespan: The timespan of the historical prices to query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stock_id:
            raise ValueError(f"Expected a non-empty value for `stock_id` but received {stock_id!r}")
        return self._get(
            path_template("/api/v2/market_data/stocks/{stock_id}/historical_prices/", stock_id=stock_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"timespan": timespan}, stock_retrieve_historical_prices_params.StockRetrieveHistoricalPricesParams
                ),
            ),
            cast_to=StockRetrieveHistoricalPricesResponse,
        )

    def retrieve_news(
        self,
        stock_id: str,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockRetrieveNewsResponse:
        """
        Get the most recent news articles relating to a `Stock`, including a summary of
        the article and a link to the original source.

        Args:
          limit: The number of articles to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stock_id:
            raise ValueError(f"Expected a non-empty value for `stock_id` but received {stock_id!r}")
        return self._get(
            path_template("/api/v2/market_data/stocks/{stock_id}/news", stock_id=stock_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"limit": limit}, stock_retrieve_news_params.StockRetrieveNewsParams),
            ),
            cast_to=StockRetrieveNewsResponse,
        )


class AsyncStocksResource(AsyncAPIResource):
    @cached_property
    def splits(self) -> AsyncSplitsResource:
        """**Corporate actions are events that affect the ownership of a `Stock`.**

        Corporate actions include dividends and stock splits.
        """
        return AsyncSplitsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStocksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dinaricrypto/dinari-api-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStocksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStocksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dinaricrypto/dinari-api-sdk-python#with_streaming_response
        """
        return AsyncStocksResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        next: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        previous: Optional[str] | Omit = omit,
        symbols: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockListResponse:
        """
        Get a list of `Stocks`.

        Args:
          limit: Number of results to return

          next: Cursor for next page

          order: Sort order

          previous: Cursor for previous page

          symbols: List of `Stock` symbols to query. If not provided, all `Stocks` are returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            StockListResponse,
            await self._get(
                "/api/v2/market_data/stocks/",
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
                            "page": page,
                            "page_size": page_size,
                            "previous": previous,
                            "symbols": symbols,
                        },
                        stock_list_params.StockListParams,
                    ),
                ),
                cast_to=cast(Any, StockListResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve_current_price(
        self,
        stock_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockRetrieveCurrentPriceResponse:
        """
        Get current price for a specified `Stock`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stock_id:
            raise ValueError(f"Expected a non-empty value for `stock_id` but received {stock_id!r}")
        return await self._get(
            path_template("/api/v2/market_data/stocks/{stock_id}/current_price", stock_id=stock_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StockRetrieveCurrentPriceResponse,
        )

    async def retrieve_current_quote(
        self,
        stock_id: str,
        *,
        feed: Optional[Literal["sip"]] | Omit = omit,
        x_api_version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockRetrieveCurrentQuoteResponse:
        """
        Get quote for a specified `Stock`.

        Args:
          feed: Requested data source for the quote. Only applies when using x-api-version: 2.
              Allowed values:

              - `null`: (default) Selects the highest quality available free data source.
              - `sip`: Consolidated quote from all U.S. exchanges (NBBO). This is a paid data
                source and incurs usage-based billing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stock_id:
            raise ValueError(f"Expected a non-empty value for `stock_id` but received {stock_id!r}")
        extra_headers = {**strip_not_given({"X-API-Version": x_api_version}), **(extra_headers or {})}
        return cast(
            StockRetrieveCurrentQuoteResponse,
            await self._get(
                path_template("/api/v2/market_data/stocks/{stock_id}/current_quote", stock_id=stock_id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {"feed": feed}, stock_retrieve_current_quote_params.StockRetrieveCurrentQuoteParams
                    ),
                ),
                cast_to=cast(
                    Any, StockRetrieveCurrentQuoteResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def retrieve_dividends(
        self,
        stock_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockRetrieveDividendsResponse:
        """
        Get a list of announced stock dividend details for a specified `Stock`.

        Note that this data applies only to actual stocks. Yield received for holding
        tokenized shares may differ from this.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stock_id:
            raise ValueError(f"Expected a non-empty value for `stock_id` but received {stock_id!r}")
        return await self._get(
            path_template("/api/v2/market_data/stocks/{stock_id}/dividends", stock_id=stock_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StockRetrieveDividendsResponse,
        )

    async def retrieve_historical_prices(
        self,
        stock_id: str,
        *,
        timespan: Literal["DAY", "WEEK", "MONTH", "YEAR"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockRetrieveHistoricalPricesResponse:
        """Get historical price data for a specified `Stock`.

        Each index in the array
        represents a single tick in a price chart.

        Args:
          timespan: The timespan of the historical prices to query.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stock_id:
            raise ValueError(f"Expected a non-empty value for `stock_id` but received {stock_id!r}")
        return await self._get(
            path_template("/api/v2/market_data/stocks/{stock_id}/historical_prices/", stock_id=stock_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"timespan": timespan}, stock_retrieve_historical_prices_params.StockRetrieveHistoricalPricesParams
                ),
            ),
            cast_to=StockRetrieveHistoricalPricesResponse,
        )

    async def retrieve_news(
        self,
        stock_id: str,
        *,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StockRetrieveNewsResponse:
        """
        Get the most recent news articles relating to a `Stock`, including a summary of
        the article and a link to the original source.

        Args:
          limit: The number of articles to return.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stock_id:
            raise ValueError(f"Expected a non-empty value for `stock_id` but received {stock_id!r}")
        return await self._get(
            path_template("/api/v2/market_data/stocks/{stock_id}/news", stock_id=stock_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"limit": limit}, stock_retrieve_news_params.StockRetrieveNewsParams),
            ),
            cast_to=StockRetrieveNewsResponse,
        )


class StocksResourceWithRawResponse:
    def __init__(self, stocks: StocksResource) -> None:
        self._stocks = stocks

        self.list = to_raw_response_wrapper(
            stocks.list,
        )
        self.retrieve_current_price = to_raw_response_wrapper(
            stocks.retrieve_current_price,
        )
        self.retrieve_current_quote = to_raw_response_wrapper(
            stocks.retrieve_current_quote,
        )
        self.retrieve_dividends = to_raw_response_wrapper(
            stocks.retrieve_dividends,
        )
        self.retrieve_historical_prices = to_raw_response_wrapper(
            stocks.retrieve_historical_prices,
        )
        self.retrieve_news = to_raw_response_wrapper(
            stocks.retrieve_news,
        )

    @cached_property
    def splits(self) -> SplitsResourceWithRawResponse:
        """**Corporate actions are events that affect the ownership of a `Stock`.**

        Corporate actions include dividends and stock splits.
        """
        return SplitsResourceWithRawResponse(self._stocks.splits)


class AsyncStocksResourceWithRawResponse:
    def __init__(self, stocks: AsyncStocksResource) -> None:
        self._stocks = stocks

        self.list = async_to_raw_response_wrapper(
            stocks.list,
        )
        self.retrieve_current_price = async_to_raw_response_wrapper(
            stocks.retrieve_current_price,
        )
        self.retrieve_current_quote = async_to_raw_response_wrapper(
            stocks.retrieve_current_quote,
        )
        self.retrieve_dividends = async_to_raw_response_wrapper(
            stocks.retrieve_dividends,
        )
        self.retrieve_historical_prices = async_to_raw_response_wrapper(
            stocks.retrieve_historical_prices,
        )
        self.retrieve_news = async_to_raw_response_wrapper(
            stocks.retrieve_news,
        )

    @cached_property
    def splits(self) -> AsyncSplitsResourceWithRawResponse:
        """**Corporate actions are events that affect the ownership of a `Stock`.**

        Corporate actions include dividends and stock splits.
        """
        return AsyncSplitsResourceWithRawResponse(self._stocks.splits)


class StocksResourceWithStreamingResponse:
    def __init__(self, stocks: StocksResource) -> None:
        self._stocks = stocks

        self.list = to_streamed_response_wrapper(
            stocks.list,
        )
        self.retrieve_current_price = to_streamed_response_wrapper(
            stocks.retrieve_current_price,
        )
        self.retrieve_current_quote = to_streamed_response_wrapper(
            stocks.retrieve_current_quote,
        )
        self.retrieve_dividends = to_streamed_response_wrapper(
            stocks.retrieve_dividends,
        )
        self.retrieve_historical_prices = to_streamed_response_wrapper(
            stocks.retrieve_historical_prices,
        )
        self.retrieve_news = to_streamed_response_wrapper(
            stocks.retrieve_news,
        )

    @cached_property
    def splits(self) -> SplitsResourceWithStreamingResponse:
        """**Corporate actions are events that affect the ownership of a `Stock`.**

        Corporate actions include dividends and stock splits.
        """
        return SplitsResourceWithStreamingResponse(self._stocks.splits)


class AsyncStocksResourceWithStreamingResponse:
    def __init__(self, stocks: AsyncStocksResource) -> None:
        self._stocks = stocks

        self.list = async_to_streamed_response_wrapper(
            stocks.list,
        )
        self.retrieve_current_price = async_to_streamed_response_wrapper(
            stocks.retrieve_current_price,
        )
        self.retrieve_current_quote = async_to_streamed_response_wrapper(
            stocks.retrieve_current_quote,
        )
        self.retrieve_dividends = async_to_streamed_response_wrapper(
            stocks.retrieve_dividends,
        )
        self.retrieve_historical_prices = async_to_streamed_response_wrapper(
            stocks.retrieve_historical_prices,
        )
        self.retrieve_news = async_to_streamed_response_wrapper(
            stocks.retrieve_news,
        )

    @cached_property
    def splits(self) -> AsyncSplitsResourceWithStreamingResponse:
        """**Corporate actions are events that affect the ownership of a `Stock`.**

        Corporate actions include dividends and stock splits.
        """
        return AsyncSplitsResourceWithStreamingResponse(self._stocks.splits)
