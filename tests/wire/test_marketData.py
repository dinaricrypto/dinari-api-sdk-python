import pytest
from .conftest import get_client, verify_request_count

from dinari_api_sdk import UnprocessableEntityError
from dinari_api_sdk.core.jsonable_encoder import jsonable_encoder


def test_marketData_get_alloys() -> None:
    """Test getAlloys endpoint with WireMock"""
    test_id = "market_data.get_alloys.0"
    client = get_client(test_id)
    client.market_data.get_alloys()
    verify_request_count(test_id, "GET", "/api/v2/market_data/alloys/", None, 1)


def test_marketData_get_alloys_throws_unprocessable_entity_error() -> None:
    """Test getAlloys endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "market_data.get_alloys.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.market_data.get_alloys()
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {
        "error_id": "error_id",
        "error": {
            "field_errors": [
                {"field_name": "field_name", "field_error": "field_error"},
                {"field_name": "field_name", "field_error": "field_error"},
            ]
        },
    }
    verify_request_count(test_id, "GET", "/api/v2/market_data/alloys/", None, 1)


def test_marketData_get_alloy_current_price() -> None:
    """Test getAlloyCurrentPrice endpoint with WireMock"""
    test_id = "market_data.get_alloy_current_price.0"
    client = get_client(test_id)
    client.market_data.get_alloy_current_price(
        alloy_id="alloy_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/market_data/alloys/alloy_id/current_price", None, 1)


def test_marketData_get_alloy_price_chart() -> None:
    """Test getAlloyPriceChart endpoint with WireMock"""
    test_id = "market_data.get_alloy_price_chart.0"
    client = get_client(test_id)
    client.market_data.get_alloy_price_chart(
        alloy_id="alloy_id",
        timespan="DAY",
    )
    verify_request_count(
        test_id, "GET", "/api/v2/market_data/alloys/alloy_id/historical_prices/", {"timespan": "DAY"}, 1
    )


def test_marketData_get_alloy_price_chart_throws_unprocessable_entity_error() -> None:
    """Test getAlloyPriceChart endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "market_data.get_alloy_price_chart.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.market_data.get_alloy_price_chart(
            alloy_id="alloy_id",
            timespan="DAY",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {
        "error_id": "error_id",
        "error": {
            "field_errors": [
                {"field_name": "field_name", "field_error": "field_error"},
                {"field_name": "field_name", "field_error": "field_error"},
            ]
        },
    }
    verify_request_count(
        test_id, "GET", "/api/v2/market_data/alloys/alloy_id/historical_prices/", {"timespan": "DAY"}, 1
    )


def test_marketData_get_stocks() -> None:
    """Test getStocks endpoint with WireMock"""
    test_id = "market_data.get_stocks.0"
    client = get_client(test_id)
    client.market_data.get_stocks()
    verify_request_count(test_id, "GET", "/api/v2/market_data/stocks/", None, 1)


def test_marketData_get_stocks_throws_unprocessable_entity_error() -> None:
    """Test getStocks endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "market_data.get_stocks.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.market_data.get_stocks()
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {
        "error_id": "error_id",
        "error": {
            "field_errors": [
                {"field_name": "field_name", "field_error": "field_error"},
                {"field_name": "field_name", "field_error": "field_error"},
            ]
        },
    }
    verify_request_count(test_id, "GET", "/api/v2/market_data/stocks/", None, 1)


def test_marketData_get_stock_current_price() -> None:
    """Test getStockCurrentPrice endpoint with WireMock"""
    test_id = "market_data.get_stock_current_price.0"
    client = get_client(test_id)
    client.market_data.get_stock_current_price(
        stock_id="stock_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/market_data/stocks/stock_id/current_price", None, 1)


def test_marketData_get_stock_current_quotes_route_v2() -> None:
    """Test getStockCurrentQuotesRouteV2 endpoint with WireMock"""
    test_id = "market_data.get_stock_current_quotes_route_v2.0"
    client = get_client(test_id)
    client.market_data.get_stock_current_quotes_route_v2(
        stock_id="stock_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/market_data/stocks/stock_id/current_quote", None, 1)


def test_marketData_get_stock_current_quotes_route_v2_throws_unprocessable_entity_error() -> None:
    """Test getStockCurrentQuotesRouteV2 endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "market_data.get_stock_current_quotes_route_v2.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.market_data.get_stock_current_quotes_route_v2(
            stock_id="stock_id",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {
        "error_id": "error_id",
        "error": {
            "field_errors": [
                {"field_name": "field_name", "field_error": "field_error"},
                {"field_name": "field_name", "field_error": "field_error"},
            ]
        },
    }
    verify_request_count(test_id, "GET", "/api/v2/market_data/stocks/stock_id/current_quote", None, 1)


def test_marketData_get_stock_price_chart() -> None:
    """Test getStockPriceChart endpoint with WireMock"""
    test_id = "market_data.get_stock_price_chart.0"
    client = get_client(test_id)
    client.market_data.get_stock_price_chart(
        stock_id="stock_id",
        timespan="DAY",
    )
    verify_request_count(
        test_id, "GET", "/api/v2/market_data/stocks/stock_id/historical_prices/", {"timespan": "DAY"}, 1
    )


def test_marketData_get_stock_price_chart_throws_unprocessable_entity_error() -> None:
    """Test getStockPriceChart endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "market_data.get_stock_price_chart.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.market_data.get_stock_price_chart(
            stock_id="stock_id",
            timespan="DAY",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {
        "error_id": "error_id",
        "error": {
            "field_errors": [
                {"field_name": "field_name", "field_error": "field_error"},
                {"field_name": "field_name", "field_error": "field_error"},
            ]
        },
    }
    verify_request_count(
        test_id, "GET", "/api/v2/market_data/stocks/stock_id/historical_prices/", {"timespan": "DAY"}, 1
    )


def test_marketData_get_stock_news_by_stock_id() -> None:
    """Test getStockNewsByStockId endpoint with WireMock"""
    test_id = "market_data.get_stock_news_by_stock_id.0"
    client = get_client(test_id)
    client.market_data.get_stock_news_by_stock_id(
        stock_id="stock_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/market_data/stocks/stock_id/news", None, 1)


def test_marketData_get_stock_news_by_stock_id_throws_unprocessable_entity_error() -> None:
    """Test getStockNewsByStockId endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "market_data.get_stock_news_by_stock_id.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.market_data.get_stock_news_by_stock_id(
            stock_id="stock_id",
        )
    assert exc_info.value.status_code == 422
    assert jsonable_encoder(exc_info.value.body) == {
        "error_id": "error_id",
        "error": {
            "field_errors": [
                {"field_name": "field_name", "field_error": "field_error"},
                {"field_name": "field_name", "field_error": "field_error"},
            ]
        },
    }
    verify_request_count(test_id, "GET", "/api/v2/market_data/stocks/stock_id/news", None, 1)


def test_marketData_get_market_hours() -> None:
    """Test getMarketHours endpoint with WireMock"""
    test_id = "market_data.get_market_hours.0"
    client = get_client(test_id)
    client.market_data.get_market_hours()
    verify_request_count(test_id, "GET", "/api/v2/market_data/market_hours/", None, 1)
