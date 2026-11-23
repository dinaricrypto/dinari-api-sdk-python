import pytest
from .conftest import get_client, verify_request_count

from dinari_api_sdk import BadRequestError, ConflictError, NotFoundError, UnprocessableEntityError
from dinari_api_sdk.core.jsonable_encoder import jsonable_encoder


def test_orders_get_entity_orders() -> None:
    """Test getEntityOrders endpoint with WireMock"""
    test_id = "orders.get_entity_orders.0"
    client = get_client(test_id)
    client.orders.get_entity_orders()
    verify_request_count(test_id, "GET", "/api/v2/orders/", None, 1)


def test_orders_get_entity_orders_throws_unprocessable_entity_error() -> None:
    """Test getEntityOrders endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "orders.get_entity_orders.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.orders.get_entity_orders()
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
    verify_request_count(test_id, "GET", "/api/v2/orders/", None, 1)


def test_orders_get_orders() -> None:
    """Test getOrders endpoint with WireMock"""
    test_id = "orders.get_orders.0"
    client = get_client(test_id)
    client.orders.get_orders(
        account_id="account_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/orders", None, 1)


def test_orders_get_orders_throws_unprocessable_entity_error() -> None:
    """Test getOrders endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "orders.get_orders.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.orders.get_orders(
            account_id="account_id",
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
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/orders", None, 1)


def test_orders_get_order_by_id() -> None:
    """Test getOrderById endpoint with WireMock"""
    test_id = "orders.get_order_by_id.0"
    client = get_client(test_id)
    client.orders.get_order_by_id(
        account_id="account_id",
        order_id="order_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/orders/order_id", None, 1)


def test_orders_create_order_cancellation() -> None:
    """Test createOrderCancellation endpoint with WireMock"""
    test_id = "orders.create_order_cancellation.0"
    client = get_client(test_id)
    client.orders.create_order_cancellation(
        account_id="account_id",
        order_id="order_id",
    )
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/orders/order_id/cancel", None, 1)


def test_orders_create_order_cancellation_throws_bad_request_error() -> None:
    """Test createOrderCancellation endpoint error response (BadRequestError) with WireMock"""
    test_id = "orders.create_order_cancellation.1"
    client = get_client(test_id)
    with pytest.raises(BadRequestError) as exc_info:
        client.orders.create_order_cancellation(
            account_id="account_id",
            order_id="order_id",
        )
    assert exc_info.value.status_code == 400
    assert jsonable_encoder(exc_info.value.body) == {"status": 1, "message": "message", "error_id": "error_id"}
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/orders/order_id/cancel", None, 1)


def test_orders_create_order_cancellation_throws_not_found_error() -> None:
    """Test createOrderCancellation endpoint error response (NotFoundError) with WireMock"""
    test_id = "orders.create_order_cancellation.2"
    client = get_client(test_id)
    with pytest.raises(NotFoundError) as exc_info:
        client.orders.create_order_cancellation(
            account_id="account_id",
            order_id="order_id",
        )
    assert exc_info.value.status_code == 404
    assert jsonable_encoder(exc_info.value.body) == {"status": 1, "message": "message", "error_id": "error_id"}
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/orders/order_id/cancel", None, 1)


def test_orders_create_order_cancellation_throws_conflict_error() -> None:
    """Test createOrderCancellation endpoint error response (ConflictError) with WireMock"""
    test_id = "orders.create_order_cancellation.3"
    client = get_client(test_id)
    with pytest.raises(ConflictError) as exc_info:
        client.orders.create_order_cancellation(
            account_id="account_id",
            order_id="order_id",
        )
    assert exc_info.value.status_code == 409
    assert jsonable_encoder(exc_info.value.body) == {"status": 1, "message": "message", "error_id": "error_id"}
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/orders/order_id/cancel", None, 1)


def test_orders_create_batch_order_cancellation() -> None:
    """Test createBatchOrderCancellation endpoint with WireMock"""
    test_id = "orders.create_batch_order_cancellation.0"
    client = get_client(test_id)
    client.orders.create_batch_order_cancellation(
        account_id="account_id",
        order_ids=["order_ids"],
    )
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/orders/cancel", None, 1)


def test_orders_create_batch_order_cancellation_throws_unprocessable_entity_error() -> None:
    """Test createBatchOrderCancellation endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "orders.create_batch_order_cancellation.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.orders.create_batch_order_cancellation(
            account_id="account_id",
            order_ids=["order_ids", "order_ids"],
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
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/orders/cancel", None, 1)


def test_orders_get_account_all_order_fulfillments() -> None:
    """Test getAccountAllOrderFulfillments endpoint with WireMock"""
    test_id = "orders.get_account_all_order_fulfillments.0"
    client = get_client(test_id)
    client.orders.get_account_all_order_fulfillments(
        account_id="account_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/order_fulfillments", None, 1)


def test_orders_get_account_all_order_fulfillments_throws_unprocessable_entity_error() -> None:
    """Test getAccountAllOrderFulfillments endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "orders.get_account_all_order_fulfillments.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.orders.get_account_all_order_fulfillments(
            account_id="account_id",
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
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/order_fulfillments", None, 1)


def test_orders_get_account_order_fulfillments() -> None:
    """Test getAccountOrderFulfillments endpoint with WireMock"""
    test_id = "orders.get_account_order_fulfillments.0"
    client = get_client(test_id)
    client.orders.get_account_order_fulfillments(
        account_id="account_id",
        order_id="order_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/orders/order_id/fulfillments", None, 1)


def test_orders_get_account_order_fulfillments_throws_unprocessable_entity_error() -> None:
    """Test getAccountOrderFulfillments endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "orders.get_account_order_fulfillments.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.orders.get_account_order_fulfillments(
            account_id="account_id",
            order_id="order_id",
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
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/orders/order_id/fulfillments", None, 1)


def test_orders_get_account_order_fulfillment_by_id() -> None:
    """Test getAccountOrderFulfillmentById endpoint with WireMock"""
    test_id = "orders.get_account_order_fulfillment_by_id.0"
    client = get_client(test_id)
    client.orders.get_account_order_fulfillment_by_id(
        account_id="account_id",
        order_fulfillment_id="order_fulfillment_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/order_fulfillments/order_fulfillment_id", None, 1)
