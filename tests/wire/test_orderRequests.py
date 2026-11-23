import pytest
from .conftest import get_client, verify_request_count

from dinari_api_sdk import UnprocessableEntityError
from dinari_api_sdk.core.jsonable_encoder import jsonable_encoder


def test_orderRequests_get_list_order_requests() -> None:
    """Test getListOrderRequests endpoint with WireMock"""
    test_id = "order_requests.get_list_order_requests.0"
    client = get_client(test_id)
    client.order_requests.get_list_order_requests(
        account_id="account_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/order_requests", None, 1)


def test_orderRequests_get_list_order_requests_throws_unprocessable_entity_error() -> None:
    """Test getListOrderRequests endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "order_requests.get_list_order_requests.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.order_requests.get_list_order_requests(
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
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/order_requests", None, 1)


def test_orderRequests_get_order_request_by_id() -> None:
    """Test getOrderRequestById endpoint with WireMock"""
    test_id = "order_requests.get_order_request_by_id.0"
    client = get_client(test_id)
    client.order_requests.get_order_request_by_id(
        account_id="account_id",
        order_request_id="order_request_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/order_requests/order_request_id", None, 1)


def test_orderRequests_create_eip155order_request_permit() -> None:
    """Test createEIP155OrderRequestPermit endpoint with WireMock"""
    test_id = "order_requests.create_eip155order_request_permit.0"
    client = get_client(test_id)
    client.order_requests.create_eip155order_request_permit(
        account_id="account_id",
        chain_id="eip155:1",
        order_tif="DAY",
        order_side="BUY",
        order_type="MARKET",
        payment_token="payment_token",
    )
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/order_requests/eip155/permit", None, 1)


def test_orderRequests_create_eip155order_request_permit_throws_unprocessable_entity_error() -> None:
    """Test createEIP155OrderRequestPermit endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "order_requests.create_eip155order_request_permit.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.order_requests.create_eip155order_request_permit(
            account_id="account_id",
            chain_id="eip155:1",
            order_tif="DAY",
            order_side="BUY",
            order_type="MARKET",
            payment_token="payment_token",
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
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/order_requests/eip155/permit", None, 1)


def test_orderRequests_create_eip155order_request_permit_transaction() -> None:
    """Test createEIP155OrderRequestPermitTransaction endpoint with WireMock"""
    test_id = "order_requests.create_eip155order_request_permit_transaction.0"
    client = get_client(test_id)
    client.order_requests.create_eip155order_request_permit_transaction(
        account_id="account_id",
        order_request_id="order_request_id",
        permit_signature="permit_signature",
    )
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/order_requests/eip155", None, 1)


def test_orderRequests_create_eip155order_request_permit_transaction_throws_unprocessable_entity_error() -> None:
    """Test createEIP155OrderRequestPermitTransaction endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "order_requests.create_eip155order_request_permit_transaction.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.order_requests.create_eip155order_request_permit_transaction(
            account_id="account_id",
            order_request_id="order_request_id",
            permit_signature="permit_signature",
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
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/order_requests/eip155", None, 1)


def test_orderRequests_create_eip155permit_transaction() -> None:
    """Test createEip155PermitTransaction endpoint with WireMock"""
    test_id = "order_requests.create_eip155permit_transaction.0"
    client = get_client(test_id)
    client.order_requests.create_eip155permit_transaction(
        account_id="account_id",
        order_request_id="order_request_id",
        permit_signature="permit_signature",
    )
    verify_request_count(
        test_id, "POST", "/api/v2/accounts/account_id/order_requests/eip155/permit_transaction", None, 1
    )


def test_orderRequests_create_eip155permit_transaction_throws_unprocessable_entity_error() -> None:
    """Test createEip155PermitTransaction endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "order_requests.create_eip155permit_transaction.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.order_requests.create_eip155permit_transaction(
            account_id="account_id",
            order_request_id="order_request_id",
            permit_signature="permit_signature",
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
        test_id, "POST", "/api/v2/accounts/account_id/order_requests/eip155/permit_transaction", None, 1
    )
