import pytest
from .conftest import get_client, verify_request_count

from dinari_api_sdk import UnprocessableEntityError
from dinari_api_sdk.core.jsonable_encoder import jsonable_encoder


def test_wallets_get_wallet() -> None:
    """Test getWallet endpoint with WireMock"""
    test_id = "wallets.get_wallet.0"
    client = get_client(test_id)
    client.wallets.get_wallet(
        account_id="account_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/accounts/account_id/wallet", None, 1)


def test_wallets_get_account_wallet_connection_nonce() -> None:
    """Test getAccountWalletConnectionNonce endpoint with WireMock"""
    test_id = "wallets.get_account_wallet_connection_nonce.0"
    client = get_client(test_id)
    client.wallets.get_account_wallet_connection_nonce(
        account_id="account_id",
        wallet_address="wallet_address",
        chain_id="eip155:0",
    )
    verify_request_count(
        test_id,
        "GET",
        "/api/v2/accounts/account_id/wallet/external/nonce",
        {"wallet_address": "wallet_address", "chain_id": "eip155:0"},
        1,
    )


def test_wallets_get_account_wallet_connection_nonce_throws_unprocessable_entity_error() -> None:
    """Test getAccountWalletConnectionNonce endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "wallets.get_account_wallet_connection_nonce.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.wallets.get_account_wallet_connection_nonce(
            account_id="account_id",
            wallet_address="wallet_address",
            chain_id="eip155:0",
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
        "/api/v2/accounts/account_id/wallet/external/nonce",
        {"wallet_address": "wallet_address", "chain_id": "eip155:0"},
        1,
    )


def test_wallets_create_account_wallet_connection() -> None:
    """Test createAccountWalletConnection endpoint with WireMock"""
    test_id = "wallets.create_account_wallet_connection.0"
    client = get_client(test_id)
    client.wallets.create_account_wallet_connection(
        account_id="account_id",
        signature="signature",
        nonce="nonce",
        wallet_address="wallet_address",
        chain_id="eip155:0",
    )
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/wallet/external", None, 1)


def test_wallets_create_account_wallet_connection_throws_unprocessable_entity_error() -> None:
    """Test createAccountWalletConnection endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "wallets.create_account_wallet_connection.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.wallets.create_account_wallet_connection(
            account_id="account_id",
            signature="signature",
            nonce="nonce",
            wallet_address="wallet_address",
            chain_id="eip155:0",
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
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/wallet/external", None, 1)


def test_wallets_create_account_wallet_internal_connection() -> None:
    """Test createAccountWalletInternalConnection endpoint with WireMock"""
    test_id = "wallets.create_account_wallet_internal_connection.0"
    client = get_client(test_id)
    client.wallets.create_account_wallet_internal_connection(
        account_id="account_id",
        wallet_address="wallet_address",
        chain_id="eip155:0",
    )
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/wallet/internal", None, 1)


def test_wallets_create_account_wallet_internal_connection_throws_unprocessable_entity_error() -> None:
    """Test createAccountWalletInternalConnection endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "wallets.create_account_wallet_internal_connection.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.wallets.create_account_wallet_internal_connection(
            account_id="account_id",
            wallet_address="wallet_address",
            chain_id="eip155:0",
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
    verify_request_count(test_id, "POST", "/api/v2/accounts/account_id/wallet/internal", None, 1)
