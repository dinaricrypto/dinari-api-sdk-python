import pytest
from .conftest import get_client, verify_request_count

from dinari_api_sdk import UnprocessableEntityError
from dinari_api_sdk.core.jsonable_encoder import jsonable_encoder


def test_corporateActions_get_stock_splits() -> None:
    """Test getStockSplits endpoint with WireMock"""
    test_id = "corporate_actions.get_stock_splits.0"
    client = get_client(test_id)
    client.corporate_actions.get_stock_splits()
    verify_request_count(test_id, "GET", "/api/v2/market_data/stocks/splits", None, 1)


def test_corporateActions_get_stock_splits_throws_unprocessable_entity_error() -> None:
    """Test getStockSplits endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "corporate_actions.get_stock_splits.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.corporate_actions.get_stock_splits()
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
    verify_request_count(test_id, "GET", "/api/v2/market_data/stocks/splits", None, 1)


def test_corporateActions_get_stock_splits_by_id() -> None:
    """Test getStockSplitsById endpoint with WireMock"""
    test_id = "corporate_actions.get_stock_splits_by_id.0"
    client = get_client(test_id)
    client.corporate_actions.get_stock_splits_by_id(
        stock_id="stock_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/market_data/stocks/stock_id/splits", None, 1)


def test_corporateActions_get_stock_splits_by_id_throws_unprocessable_entity_error() -> None:
    """Test getStockSplitsById endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "corporate_actions.get_stock_splits_by_id.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.corporate_actions.get_stock_splits_by_id(
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
    verify_request_count(test_id, "GET", "/api/v2/market_data/stocks/stock_id/splits", None, 1)


def test_corporateActions_get_stock_dividends_by_stock_id() -> None:
    """Test getStockDividendsByStockId endpoint with WireMock"""
    test_id = "corporate_actions.get_stock_dividends_by_stock_id.0"
    client = get_client(test_id)
    client.corporate_actions.get_stock_dividends_by_stock_id(
        stock_id="stock_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/market_data/stocks/stock_id/dividends", None, 1)
