# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from dinari_api_sdk import Dinari, AsyncDinari
from dinari_api_sdk.types.v2.market_data import (
    AlloyListResponse,
    AlloyRetrieveCurrentPriceResponse,
    AlloyRetrieveHistoricalPricesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAlloys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Dinari) -> None:
        alloy = client.v2.market_data.alloys.list()
        assert_matches_type(AlloyListResponse, alloy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Dinari) -> None:
        alloy = client.v2.market_data.alloys.list(
            limit=20,
            next="next",
            order="asc",
            previous="previous",
            symbols=["string"],
        )
        assert_matches_type(AlloyListResponse, alloy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Dinari) -> None:
        response = client.v2.market_data.alloys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alloy = response.parse()
        assert_matches_type(AlloyListResponse, alloy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Dinari) -> None:
        with client.v2.market_data.alloys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alloy = response.parse()
            assert_matches_type(AlloyListResponse, alloy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_current_price(self, client: Dinari) -> None:
        alloy = client.v2.market_data.alloys.retrieve_current_price(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AlloyRetrieveCurrentPriceResponse, alloy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_current_price(self, client: Dinari) -> None:
        response = client.v2.market_data.alloys.with_raw_response.retrieve_current_price(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alloy = response.parse()
        assert_matches_type(AlloyRetrieveCurrentPriceResponse, alloy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_current_price(self, client: Dinari) -> None:
        with client.v2.market_data.alloys.with_streaming_response.retrieve_current_price(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alloy = response.parse()
            assert_matches_type(AlloyRetrieveCurrentPriceResponse, alloy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_current_price(self, client: Dinari) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alloy_id` but received ''"):
            client.v2.market_data.alloys.with_raw_response.retrieve_current_price(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_historical_prices(self, client: Dinari) -> None:
        alloy = client.v2.market_data.alloys.retrieve_historical_prices(
            alloy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            timespan="DAY",
        )
        assert_matches_type(AlloyRetrieveHistoricalPricesResponse, alloy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_historical_prices(self, client: Dinari) -> None:
        response = client.v2.market_data.alloys.with_raw_response.retrieve_historical_prices(
            alloy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            timespan="DAY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alloy = response.parse()
        assert_matches_type(AlloyRetrieveHistoricalPricesResponse, alloy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_historical_prices(self, client: Dinari) -> None:
        with client.v2.market_data.alloys.with_streaming_response.retrieve_historical_prices(
            alloy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            timespan="DAY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alloy = response.parse()
            assert_matches_type(AlloyRetrieveHistoricalPricesResponse, alloy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_historical_prices(self, client: Dinari) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alloy_id` but received ''"):
            client.v2.market_data.alloys.with_raw_response.retrieve_historical_prices(
                alloy_id="",
                timespan="DAY",
            )


class TestAsyncAlloys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncDinari) -> None:
        alloy = await async_client.v2.market_data.alloys.list()
        assert_matches_type(AlloyListResponse, alloy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncDinari) -> None:
        alloy = await async_client.v2.market_data.alloys.list(
            limit=20,
            next="next",
            order="asc",
            previous="previous",
            symbols=["string"],
        )
        assert_matches_type(AlloyListResponse, alloy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncDinari) -> None:
        response = await async_client.v2.market_data.alloys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alloy = await response.parse()
        assert_matches_type(AlloyListResponse, alloy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncDinari) -> None:
        async with async_client.v2.market_data.alloys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alloy = await response.parse()
            assert_matches_type(AlloyListResponse, alloy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_current_price(self, async_client: AsyncDinari) -> None:
        alloy = await async_client.v2.market_data.alloys.retrieve_current_price(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AlloyRetrieveCurrentPriceResponse, alloy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_current_price(self, async_client: AsyncDinari) -> None:
        response = await async_client.v2.market_data.alloys.with_raw_response.retrieve_current_price(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alloy = await response.parse()
        assert_matches_type(AlloyRetrieveCurrentPriceResponse, alloy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_current_price(self, async_client: AsyncDinari) -> None:
        async with async_client.v2.market_data.alloys.with_streaming_response.retrieve_current_price(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alloy = await response.parse()
            assert_matches_type(AlloyRetrieveCurrentPriceResponse, alloy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_current_price(self, async_client: AsyncDinari) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alloy_id` but received ''"):
            await async_client.v2.market_data.alloys.with_raw_response.retrieve_current_price(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_historical_prices(self, async_client: AsyncDinari) -> None:
        alloy = await async_client.v2.market_data.alloys.retrieve_historical_prices(
            alloy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            timespan="DAY",
        )
        assert_matches_type(AlloyRetrieveHistoricalPricesResponse, alloy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_historical_prices(self, async_client: AsyncDinari) -> None:
        response = await async_client.v2.market_data.alloys.with_raw_response.retrieve_historical_prices(
            alloy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            timespan="DAY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        alloy = await response.parse()
        assert_matches_type(AlloyRetrieveHistoricalPricesResponse, alloy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_historical_prices(self, async_client: AsyncDinari) -> None:
        async with async_client.v2.market_data.alloys.with_streaming_response.retrieve_historical_prices(
            alloy_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            timespan="DAY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            alloy = await response.parse()
            assert_matches_type(AlloyRetrieveHistoricalPricesResponse, alloy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_historical_prices(self, async_client: AsyncDinari) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `alloy_id` but received ''"):
            await async_client.v2.market_data.alloys.with_raw_response.retrieve_historical_prices(
                alloy_id="",
                timespan="DAY",
            )
