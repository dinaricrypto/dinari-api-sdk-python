import pytest
from .conftest import get_client, verify_request_count

from dinari_api_sdk import UnprocessableEntityError
from dinari_api_sdk.core.jsonable_encoder import jsonable_encoder


def test_withdrawals_get_account_withdrawal_requests() -> None:
    """Test getAccountWithdrawalRequests endpoint with WireMock"""
    test_id = "withdrawals.get_account_withdrawal_requests.0"
    client = get_client(test_id)
    client.withdrawals.get_account_withdrawal_requests(
        account_id="account_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/withdrawal_requests", None, 1)


def test_withdrawals_get_account_withdrawal_requests_throws_unprocessable_entity_error() -> None:
    """Test getAccountWithdrawalRequests endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "withdrawals.get_account_withdrawal_requests.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.withdrawals.get_account_withdrawal_requests(
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
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/withdrawal_requests", None, 1)


def test_withdrawals_create_account_withdrawal_requests() -> None:
    """Test createAccountWithdrawalRequests endpoint with WireMock"""
    test_id = "withdrawals.create_account_withdrawal_requests.0"
    client = get_client(test_id)
    client.withdrawals.create_account_withdrawal_requests(
        account_id="account_id",
        recipient_account_id="recipient_account_id",
        payment_token_quantity=1.1,
    )
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/withdrawal_requests", None, 1)


def test_withdrawals_create_account_withdrawal_requests_throws_unprocessable_entity_error() -> None:
    """Test createAccountWithdrawalRequests endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "withdrawals.create_account_withdrawal_requests.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.withdrawals.create_account_withdrawal_requests(
            account_id="account_id",
            recipient_account_id="recipient_account_id",
            payment_token_quantity=1.1,
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
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/withdrawal_requests", None, 1)


def test_withdrawals_get_account_withdrawal_request() -> None:
    """Test getAccountWithdrawalRequest endpoint with WireMock"""
    test_id = "withdrawals.get_account_withdrawal_request.0"
    client = get_client(test_id)
    client.withdrawals.get_account_withdrawal_request(
        account_id="account_id",
        withdrawal_request_id="withdrawal_request_id",
    )
    verify_request_count(
        test_id, "GET", "/api/v2/accounts/account_id/withdrawal_requests/withdrawal_request_id", None, 1
    )


def test_withdrawals_get_account_withdrawals() -> None:
    """Test getAccountWithdrawals endpoint with WireMock"""
    test_id = "withdrawals.get_account_withdrawals.0"
    client = get_client(test_id)
    client.withdrawals.get_account_withdrawals(
        account_id="account_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/withdrawals", None, 1)


def test_withdrawals_get_account_withdrawals_throws_unprocessable_entity_error() -> None:
    """Test getAccountWithdrawals endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "withdrawals.get_account_withdrawals.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.withdrawals.get_account_withdrawals(
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
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/withdrawals", None, 1)


def test_withdrawals_get_account_withdrawal() -> None:
    """Test getAccountWithdrawal endpoint with WireMock"""
    test_id = "withdrawals.get_account_withdrawal.0"
    client = get_client(test_id)
    client.withdrawals.get_account_withdrawal(
        account_id="account_id",
        withdrawal_id="withdrawal_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/withdrawals/withdrawal_id", None, 1)
