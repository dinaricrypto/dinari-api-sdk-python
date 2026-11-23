import datetime

import pytest
from .conftest import get_client, verify_request_count

from dinari_api_sdk import UnprocessableEntityError
from dinari_api_sdk.core.jsonable_encoder import jsonable_encoder


def test_accounts_get_entity_accounts() -> None:
    """Test getEntityAccounts endpoint with WireMock"""
    test_id = "accounts.get_entity_accounts.0"
    client = get_client(test_id)
    client.accounts.get_entity_accounts(
        entity_id="entity_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/entities/entity_id/accounts", None, 1)


def test_accounts_get_entity_accounts_throws_unprocessable_entity_error() -> None:
    """Test getEntityAccounts endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "accounts.get_entity_accounts.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.accounts.get_entity_accounts(
            entity_id="entity_id",
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
    verify_request_count(test_id, "GET", "/api/v2/entities/entity_id/accounts", None, 1)


def test_accounts_create_entity_accounts() -> None:
    """Test createEntityAccounts endpoint with WireMock"""
    test_id = "accounts.create_entity_accounts.0"
    client = get_client(test_id)
    client.accounts.create_entity_accounts(
        entity_id="entity_id",
    )
    verify_request_count(test_id, "POST", "/api/v2/entities/entity_id/accounts", None, 1)


def test_accounts_create_entity_accounts_throws_unprocessable_entity_error() -> None:
    """Test createEntityAccounts endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "accounts.create_entity_accounts.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.accounts.create_entity_accounts(
            entity_id="entity_id",
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
    verify_request_count(test_id, "POST", "/api/v2/entities/entity_id/accounts", None, 1)


def test_accounts_get_account() -> None:
    """Test getAccount endpoint with WireMock"""
    test_id = "accounts.get_account.0"
    client = get_client(test_id)
    client.accounts.get_account(
        account_id="account_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id", None, 1)


def test_accounts_create_account_deactivation() -> None:
    """Test createAccountDeactivation endpoint with WireMock"""
    test_id = "accounts.create_account_deactivation.0"
    client = get_client(test_id)
    client.accounts.create_account_deactivation(
        account_id="account_id",
    )
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/deactivate", None, 1)


def test_accounts_get_account_portfolio() -> None:
    """Test getAccountPortfolio endpoint with WireMock"""
    test_id = "accounts.get_account_portfolio.0"
    client = get_client(test_id)
    client.accounts.get_account_portfolio(
        account_id="account_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/portfolio", None, 1)


def test_accounts_get_account_portfolio_throws_unprocessable_entity_error() -> None:
    """Test getAccountPortfolio endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "accounts.get_account_portfolio.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.accounts.get_account_portfolio(
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
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/portfolio", None, 1)


def test_accounts_get_account_cash() -> None:
    """Test getAccountCash endpoint with WireMock"""
    test_id = "accounts.get_account_cash.0"
    client = get_client(test_id)
    client.accounts.get_account_cash(
        account_id="account_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/cash", None, 1)


def test_accounts_get_account_interest_payments() -> None:
    """Test getAccountInterestPayments endpoint with WireMock"""
    test_id = "accounts.get_account_interest_payments.0"
    client = get_client(test_id)
    client.accounts.get_account_interest_payments(
        account_id="account_id",
        start_date=datetime.date.fromisoformat("2023-01-15"),
        end_date=datetime.date.fromisoformat("2023-01-15"),
    )
    verify_request_count(
        test_id,
        "GET",
        "/api/v2/accounts/account_id/interest_payments",
        {"start_date": "2023-01-15", "end_date": "2023-01-15"},
        1,
    )


def test_accounts_get_account_interest_payments_throws_unprocessable_entity_error() -> None:
    """Test getAccountInterestPayments endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "accounts.get_account_interest_payments.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.accounts.get_account_interest_payments(
            account_id="account_id",
            start_date=datetime.date.fromisoformat("2023-01-15"),
            end_date=datetime.date.fromisoformat("2023-01-15"),
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
        test_id,
        "GET",
        "/api/v2/accounts/account_id/interest_payments",
        {"start_date": "2023-01-15", "end_date": "2023-01-15"},
        1,
    )


def test_accounts_get_account_dividend_payments() -> None:
    """Test getAccountDividendPayments endpoint with WireMock"""
    test_id = "accounts.get_account_dividend_payments.0"
    client = get_client(test_id)
    client.accounts.get_account_dividend_payments(
        account_id="account_id",
        start_date=datetime.date.fromisoformat("2023-01-15"),
        end_date=datetime.date.fromisoformat("2023-01-15"),
    )
    verify_request_count(
        test_id,
        "GET",
        "/api/v2/accounts/account_id/dividend_payments",
        {"start_date": "2023-01-15", "end_date": "2023-01-15"},
        1,
    )


def test_accounts_get_account_dividend_payments_throws_unprocessable_entity_error() -> None:
    """Test getAccountDividendPayments endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "accounts.get_account_dividend_payments.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.accounts.get_account_dividend_payments(
            account_id="account_id",
            start_date=datetime.date.fromisoformat("2023-01-15"),
            end_date=datetime.date.fromisoformat("2023-01-15"),
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
        test_id,
        "GET",
        "/api/v2/accounts/account_id/dividend_payments",
        {"start_date": "2023-01-15", "end_date": "2023-01-15"},
        1,
    )


def test_accounts_create_account_faucet() -> None:
    """Test createAccountFaucet endpoint with WireMock"""
    test_id = "accounts.create_account_faucet.0"
    client = get_client(test_id)
    client.accounts.create_account_faucet(
        account_id="account_id",
    )
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/faucet", None, 1)


def test_accounts_create_account_faucet_throws_unprocessable_entity_error() -> None:
    """Test createAccountFaucet endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "accounts.create_account_faucet.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.accounts.create_account_faucet(
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
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/faucet", None, 1)


def test_accounts_get_brokerage_account_activities() -> None:
    """Test getBrokerageAccountActivities endpoint with WireMock"""
    test_id = "accounts.get_brokerage_account_activities.0"
    client = get_client(test_id)
    client.accounts.get_brokerage_account_activities(
        account_id="account_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/activities/brokerage", None, 1)


def test_accounts_get_brokerage_account_activities_throws_unprocessable_entity_error() -> None:
    """Test getBrokerageAccountActivities endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "accounts.get_brokerage_account_activities.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.accounts.get_brokerage_account_activities(
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
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/activities/brokerage", None, 1)


def test_accounts_get_token_transfers() -> None:
    """Test getTokenTransfers endpoint with WireMock"""
    test_id = "accounts.get_token_transfers.0"
    client = get_client(test_id)
    client.accounts.get_token_transfers(
        account_id="account_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/token_transfers", None, 1)


def test_accounts_get_token_transfers_throws_unprocessable_entity_error() -> None:
    """Test getTokenTransfers endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "accounts.get_token_transfers.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.accounts.get_token_transfers(
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
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/token_transfers", None, 1)


def test_accounts_create_token_transfers() -> None:
    """Test createTokenTransfers endpoint with WireMock"""
    test_id = "accounts.create_token_transfers.0"
    client = get_client(test_id)
    client.accounts.create_token_transfers(
        account_id="account_id",
        recipient_account_id="recipient_account_id",
        token_address="token_address",
        quantity=1.1,
    )
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/token_transfers", None, 1)


def test_accounts_create_token_transfers_throws_unprocessable_entity_error() -> None:
    """Test createTokenTransfers endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "accounts.create_token_transfers.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.accounts.create_token_transfers(
            account_id="account_id",
            recipient_account_id="recipient_account_id",
            token_address="token_address",
            quantity=1.1,
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
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/token_transfers", None, 1)


def test_accounts_get_token_transfer() -> None:
    """Test getTokenTransfer endpoint with WireMock"""
    test_id = "accounts.get_token_transfer.0"
    client = get_client(test_id)
    client.accounts.get_token_transfer(
        account_id="account_id",
        transfer_id="transfer_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/token_transfers/transfer_id", None, 1)
