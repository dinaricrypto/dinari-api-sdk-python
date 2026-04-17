# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Optional, cast
from typing_extensions import Literal

import httpx

from ...types import v2_list_orders_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from .accounts.accounts import (
    AccountsResource,
    AsyncAccountsResource,
    AccountsResourceWithRawResponse,
    AsyncAccountsResourceWithRawResponse,
    AccountsResourceWithStreamingResponse,
    AsyncAccountsResourceWithStreamingResponse,
)
from .entities.entities import (
    EntitiesResource,
    AsyncEntitiesResource,
    EntitiesResourceWithRawResponse,
    AsyncEntitiesResourceWithRawResponse,
    EntitiesResourceWithStreamingResponse,
    AsyncEntitiesResourceWithStreamingResponse,
)
from .market_data.market_data import (
    MarketDataResource,
    AsyncMarketDataResource,
    MarketDataResourceWithRawResponse,
    AsyncMarketDataResourceWithRawResponse,
    MarketDataResourceWithStreamingResponse,
    AsyncMarketDataResourceWithStreamingResponse,
)
from ...types.v2_list_orders_response import V2ListOrdersResponse

__all__ = ["V2Resource", "AsyncV2Resource"]


class V2Resource(SyncAPIResource):
    """**`Orders` represent the buying and selling of assets under an `Account`.**

    For `Accounts` using self-custodied `Wallets`, `Orders` are created and fulfilled by making calls to Dinari's smart contracts, or using the *Proxied Orders* methods.

    For `Accounts` using managed `Wallets`, `Orders` are created and fulfilled by using the `Managed Orders` methods, which then create the corresponding transactions on the blockchain.
    """

    @cached_property
    def market_data(self) -> MarketDataResource:
        """
        **Dinari provides basic market data for `Stocks` and `Alloys` that are available to transact on.**

        This data is provided on a best-effort basis and we recommend using a dedicated provider for more intensive market data needs.
        """
        return MarketDataResource(self._client)

    @cached_property
    def entities(self) -> EntitiesResource:
        """
        **`Entities` represent a business or organization that uses the API, and their customers.**

        Dinari Partners are represented as an organization `Entity` in the API, with their own accounts.
        Individual customers of Partner `Entities` are also represented as `Entities` in the API, which are managed by the Partner `Entity`.
        """
        return EntitiesResource(self._client)

    @cached_property
    def accounts(self) -> AccountsResource:
        """**`Accounts` represent the financial accounts of an `Entity`.**

        `Orders`, dividends, and other transactions are associated with an `Account`.
        """
        return AccountsResource(self._client)

    @cached_property
    def with_raw_response(self) -> V2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dinaricrypto/dinari-api-sdk-python#accessing-raw-response-data-eg-headers
        """
        return V2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dinaricrypto/dinari-api-sdk-python#with_streaming_response
        """
        return V2ResourceWithStreamingResponse(self)

    def list_orders(
        self,
        *,
        chain_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        next: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_fulfillment_transaction_hash: Optional[str] | Omit = omit,
        order_request_id: Optional[str] | Omit = omit,
        order_transaction_hash: Optional[str] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        previous: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListOrdersResponse:
        """Get a list of all `Orders` under the `Entity`.

        Optionally `Orders` can be
        transaction hash or fulfillment transaction hash.

        Args:
          chain_id: CAIP-2 formatted chain ID of the blockchain the `Order` was made on.

          limit: Number of results to return

          next: Cursor for next page

          order: Sort order

          order_fulfillment_transaction_hash: Fulfillment transaction hash of the `Order`.

          order_request_id: Order Request ID for the `Order`

          order_transaction_hash: Transaction hash of the `Order`.

          previous: Cursor for previous page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            V2ListOrdersResponse,
            self._get(
                "/api/v2/orders/",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "chain_id": chain_id,
                            "limit": limit,
                            "next": next,
                            "order": order,
                            "order_fulfillment_transaction_hash": order_fulfillment_transaction_hash,
                            "order_request_id": order_request_id,
                            "order_transaction_hash": order_transaction_hash,
                            "page": page,
                            "page_size": page_size,
                            "previous": previous,
                        },
                        v2_list_orders_params.V2ListOrdersParams,
                    ),
                ),
                cast_to=cast(
                    Any, V2ListOrdersResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncV2Resource(AsyncAPIResource):
    """**`Orders` represent the buying and selling of assets under an `Account`.**

    For `Accounts` using self-custodied `Wallets`, `Orders` are created and fulfilled by making calls to Dinari's smart contracts, or using the *Proxied Orders* methods.

    For `Accounts` using managed `Wallets`, `Orders` are created and fulfilled by using the `Managed Orders` methods, which then create the corresponding transactions on the blockchain.
    """

    @cached_property
    def market_data(self) -> AsyncMarketDataResource:
        """
        **Dinari provides basic market data for `Stocks` and `Alloys` that are available to transact on.**

        This data is provided on a best-effort basis and we recommend using a dedicated provider for more intensive market data needs.
        """
        return AsyncMarketDataResource(self._client)

    @cached_property
    def entities(self) -> AsyncEntitiesResource:
        """
        **`Entities` represent a business or organization that uses the API, and their customers.**

        Dinari Partners are represented as an organization `Entity` in the API, with their own accounts.
        Individual customers of Partner `Entities` are also represented as `Entities` in the API, which are managed by the Partner `Entity`.
        """
        return AsyncEntitiesResource(self._client)

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        """**`Accounts` represent the financial accounts of an `Entity`.**

        `Orders`, dividends, and other transactions are associated with an `Account`.
        """
        return AsyncAccountsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV2ResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/dinaricrypto/dinari-api-sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncV2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV2ResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/dinaricrypto/dinari-api-sdk-python#with_streaming_response
        """
        return AsyncV2ResourceWithStreamingResponse(self)

    async def list_orders(
        self,
        *,
        chain_id: Optional[str] | Omit = omit,
        limit: int | Omit = omit,
        next: Optional[str] | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        order_fulfillment_transaction_hash: Optional[str] | Omit = omit,
        order_request_id: Optional[str] | Omit = omit,
        order_transaction_hash: Optional[str] | Omit = omit,
        page: int | Omit = omit,
        page_size: int | Omit = omit,
        previous: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> V2ListOrdersResponse:
        """Get a list of all `Orders` under the `Entity`.

        Optionally `Orders` can be
        transaction hash or fulfillment transaction hash.

        Args:
          chain_id: CAIP-2 formatted chain ID of the blockchain the `Order` was made on.

          limit: Number of results to return

          next: Cursor for next page

          order: Sort order

          order_fulfillment_transaction_hash: Fulfillment transaction hash of the `Order`.

          order_request_id: Order Request ID for the `Order`

          order_transaction_hash: Transaction hash of the `Order`.

          previous: Cursor for previous page

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            V2ListOrdersResponse,
            await self._get(
                "/api/v2/orders/",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "chain_id": chain_id,
                            "limit": limit,
                            "next": next,
                            "order": order,
                            "order_fulfillment_transaction_hash": order_fulfillment_transaction_hash,
                            "order_request_id": order_request_id,
                            "order_transaction_hash": order_transaction_hash,
                            "page": page,
                            "page_size": page_size,
                            "previous": previous,
                        },
                        v2_list_orders_params.V2ListOrdersParams,
                    ),
                ),
                cast_to=cast(
                    Any, V2ListOrdersResponse
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class V2ResourceWithRawResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.list_orders = to_raw_response_wrapper(
            v2.list_orders,
        )

    @cached_property
    def market_data(self) -> MarketDataResourceWithRawResponse:
        """
        **Dinari provides basic market data for `Stocks` and `Alloys` that are available to transact on.**

        This data is provided on a best-effort basis and we recommend using a dedicated provider for more intensive market data needs.
        """
        return MarketDataResourceWithRawResponse(self._v2.market_data)

    @cached_property
    def entities(self) -> EntitiesResourceWithRawResponse:
        """
        **`Entities` represent a business or organization that uses the API, and their customers.**

        Dinari Partners are represented as an organization `Entity` in the API, with their own accounts.
        Individual customers of Partner `Entities` are also represented as `Entities` in the API, which are managed by the Partner `Entity`.
        """
        return EntitiesResourceWithRawResponse(self._v2.entities)

    @cached_property
    def accounts(self) -> AccountsResourceWithRawResponse:
        """**`Accounts` represent the financial accounts of an `Entity`.**

        `Orders`, dividends, and other transactions are associated with an `Account`.
        """
        return AccountsResourceWithRawResponse(self._v2.accounts)


class AsyncV2ResourceWithRawResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.list_orders = async_to_raw_response_wrapper(
            v2.list_orders,
        )

    @cached_property
    def market_data(self) -> AsyncMarketDataResourceWithRawResponse:
        """
        **Dinari provides basic market data for `Stocks` and `Alloys` that are available to transact on.**

        This data is provided on a best-effort basis and we recommend using a dedicated provider for more intensive market data needs.
        """
        return AsyncMarketDataResourceWithRawResponse(self._v2.market_data)

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithRawResponse:
        """
        **`Entities` represent a business or organization that uses the API, and their customers.**

        Dinari Partners are represented as an organization `Entity` in the API, with their own accounts.
        Individual customers of Partner `Entities` are also represented as `Entities` in the API, which are managed by the Partner `Entity`.
        """
        return AsyncEntitiesResourceWithRawResponse(self._v2.entities)

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithRawResponse:
        """**`Accounts` represent the financial accounts of an `Entity`.**

        `Orders`, dividends, and other transactions are associated with an `Account`.
        """
        return AsyncAccountsResourceWithRawResponse(self._v2.accounts)


class V2ResourceWithStreamingResponse:
    def __init__(self, v2: V2Resource) -> None:
        self._v2 = v2

        self.list_orders = to_streamed_response_wrapper(
            v2.list_orders,
        )

    @cached_property
    def market_data(self) -> MarketDataResourceWithStreamingResponse:
        """
        **Dinari provides basic market data for `Stocks` and `Alloys` that are available to transact on.**

        This data is provided on a best-effort basis and we recommend using a dedicated provider for more intensive market data needs.
        """
        return MarketDataResourceWithStreamingResponse(self._v2.market_data)

    @cached_property
    def entities(self) -> EntitiesResourceWithStreamingResponse:
        """
        **`Entities` represent a business or organization that uses the API, and their customers.**

        Dinari Partners are represented as an organization `Entity` in the API, with their own accounts.
        Individual customers of Partner `Entities` are also represented as `Entities` in the API, which are managed by the Partner `Entity`.
        """
        return EntitiesResourceWithStreamingResponse(self._v2.entities)

    @cached_property
    def accounts(self) -> AccountsResourceWithStreamingResponse:
        """**`Accounts` represent the financial accounts of an `Entity`.**

        `Orders`, dividends, and other transactions are associated with an `Account`.
        """
        return AccountsResourceWithStreamingResponse(self._v2.accounts)


class AsyncV2ResourceWithStreamingResponse:
    def __init__(self, v2: AsyncV2Resource) -> None:
        self._v2 = v2

        self.list_orders = async_to_streamed_response_wrapper(
            v2.list_orders,
        )

    @cached_property
    def market_data(self) -> AsyncMarketDataResourceWithStreamingResponse:
        """
        **Dinari provides basic market data for `Stocks` and `Alloys` that are available to transact on.**

        This data is provided on a best-effort basis and we recommend using a dedicated provider for more intensive market data needs.
        """
        return AsyncMarketDataResourceWithStreamingResponse(self._v2.market_data)

    @cached_property
    def entities(self) -> AsyncEntitiesResourceWithStreamingResponse:
        """
        **`Entities` represent a business or organization that uses the API, and their customers.**

        Dinari Partners are represented as an organization `Entity` in the API, with their own accounts.
        Individual customers of Partner `Entities` are also represented as `Entities` in the API, which are managed by the Partner `Entity`.
        """
        return AsyncEntitiesResourceWithStreamingResponse(self._v2.entities)

    @cached_property
    def accounts(self) -> AsyncAccountsResourceWithStreamingResponse:
        """**`Accounts` represent the financial accounts of an `Entity`.**

        `Orders`, dividends, and other transactions are associated with an `Account`.
        """
        return AsyncAccountsResourceWithStreamingResponse(self._v2.accounts)
