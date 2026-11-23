import pytest
from .conftest import get_client, verify_request_count

from dinari_api_sdk import LockedError, UnprocessableEntityError
from dinari_api_sdk.core.jsonable_encoder import jsonable_encoder


def test_managedOrders_create_market_buy_managed_order_request() -> None:
    """Test createMarketBuyManagedOrderRequest endpoint with WireMock"""
    test_id = "managed_orders.create_market_buy_managed_order_request.0"
    client = get_client(test_id)
    client.managed_orders.create_market_buy_managed_order_request(
        account_id="account_id",
        payment_amount=1.1,
    )
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/order_requests/market_buy", None, 1)


def test_managedOrders_create_market_buy_managed_order_request_throws_unprocessable_entity_error() -> None:
    """Test createMarketBuyManagedOrderRequest endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "managed_orders.create_market_buy_managed_order_request.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.managed_orders.create_market_buy_managed_order_request(
            account_id="account_id",
            payment_amount=1.1,
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
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/order_requests/market_buy", None, 1)


def test_managedOrders_create_market_buy_managed_order_request_throws_locked_error() -> None:
    """Test createMarketBuyManagedOrderRequest endpoint error response (LockedError) with WireMock"""
    test_id = "managed_orders.create_market_buy_managed_order_request.2"
    client = get_client(test_id)
    with pytest.raises(LockedError) as exc_info:
        client.managed_orders.create_market_buy_managed_order_request(
            account_id="account_id",
            payment_amount=1.1,
        )
    assert exc_info.value.status_code == 423
    assert jsonable_encoder(exc_info.value.body) == {"status": 1, "message": "message", "error_id": "error_id"}
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/order_requests/market_buy", None, 1)


def test_managedOrders_create_market_sell_managed_order_request() -> None:
    """Test createMarketSellManagedOrderRequest endpoint with WireMock"""
    test_id = "managed_orders.create_market_sell_managed_order_request.0"
    client = get_client(test_id)
    client.managed_orders.create_market_sell_managed_order_request(
        account_id="account_id",
        asset_quantity=1.1,
    )
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/order_requests/market_sell", None, 1)


def test_managedOrders_create_market_sell_managed_order_request_throws_unprocessable_entity_error() -> None:
    """Test createMarketSellManagedOrderRequest endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "managed_orders.create_market_sell_managed_order_request.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.managed_orders.create_market_sell_managed_order_request(
            account_id="account_id",
            asset_quantity=1.1,
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
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/order_requests/market_sell", None, 1)


def test_managedOrders_create_market_sell_managed_order_request_throws_locked_error() -> None:
    """Test createMarketSellManagedOrderRequest endpoint error response (LockedError) with WireMock"""
    test_id = "managed_orders.create_market_sell_managed_order_request.2"
    client = get_client(test_id)
    with pytest.raises(LockedError) as exc_info:
        client.managed_orders.create_market_sell_managed_order_request(
            account_id="account_id",
            asset_quantity=1.1,
        )
    assert exc_info.value.status_code == 423
    assert jsonable_encoder(exc_info.value.body) == {"status": 1, "message": "message", "error_id": "error_id"}
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/order_requests/market_sell", None, 1)


def test_managedOrders_create_limit_buy_managed_order_request() -> None:
    """Test createLimitBuyManagedOrderRequest endpoint with WireMock"""
    test_id = "managed_orders.create_limit_buy_managed_order_request.0"
    client = get_client(test_id)
    client.managed_orders.create_limit_buy_managed_order_request(
        account_id="account_id",
        asset_quantity=1.1,
        limit_price=1.1,
    )
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/order_requests/limit_buy", None, 1)


def test_managedOrders_create_limit_buy_managed_order_request_throws_unprocessable_entity_error() -> None:
    """Test createLimitBuyManagedOrderRequest endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "managed_orders.create_limit_buy_managed_order_request.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.managed_orders.create_limit_buy_managed_order_request(
            account_id="account_id",
            asset_quantity=1.1,
            limit_price=1.1,
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
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/order_requests/limit_buy", None, 1)


def test_managedOrders_create_limit_buy_managed_order_request_throws_locked_error() -> None:
    """Test createLimitBuyManagedOrderRequest endpoint error response (LockedError) with WireMock"""
    test_id = "managed_orders.create_limit_buy_managed_order_request.2"
    client = get_client(test_id)
    with pytest.raises(LockedError) as exc_info:
        client.managed_orders.create_limit_buy_managed_order_request(
            account_id="account_id",
            asset_quantity=1.1,
            limit_price=1.1,
        )
    assert exc_info.value.status_code == 423
    assert jsonable_encoder(exc_info.value.body) == {"status": 1, "message": "message", "error_id": "error_id"}
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/order_requests/limit_buy", None, 1)


def test_managedOrders_create_limit_sell_managed_order_request() -> None:
    """Test createLimitSellManagedOrderRequest endpoint with WireMock"""
    test_id = "managed_orders.create_limit_sell_managed_order_request.0"
    client = get_client(test_id)
    client.managed_orders.create_limit_sell_managed_order_request(
        account_id="account_id",
        asset_quantity=1.1,
        limit_price=1.1,
    )
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/order_requests/limit_sell", None, 1)


def test_managedOrders_create_limit_sell_managed_order_request_throws_unprocessable_entity_error() -> None:
    """Test createLimitSellManagedOrderRequest endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "managed_orders.create_limit_sell_managed_order_request.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.managed_orders.create_limit_sell_managed_order_request(
            account_id="account_id",
            asset_quantity=1.1,
            limit_price=1.1,
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
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/order_requests/limit_sell", None, 1)


def test_managedOrders_create_limit_sell_managed_order_request_throws_locked_error() -> None:
    """Test createLimitSellManagedOrderRequest endpoint error response (LockedError) with WireMock"""
    test_id = "managed_orders.create_limit_sell_managed_order_request.2"
    client = get_client(test_id)
    with pytest.raises(LockedError) as exc_info:
        client.managed_orders.create_limit_sell_managed_order_request(
            account_id="account_id",
            asset_quantity=1.1,
            limit_price=1.1,
        )
    assert exc_info.value.status_code == 423
    assert jsonable_encoder(exc_info.value.body) == {"status": 1, "message": "message", "error_id": "error_id"}
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/order_requests/limit_sell", None, 1)
