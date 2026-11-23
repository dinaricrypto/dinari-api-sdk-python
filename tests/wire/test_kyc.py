import pytest
from .conftest import get_client, verify_request_count

from dinari_api_sdk import BaselineKycCheckDataV0, CreateKycInput_Baseline, UnprocessableEntityError
from dinari_api_sdk.core.jsonable_encoder import jsonable_encoder


def test_kyc_get_entity_kyc() -> None:
    """Test getEntityKyc endpoint with WireMock"""
    test_id = "kyc.get_entity_kyc.0"
    client = get_client(test_id)
    client.kyc.get_entity_kyc(
        entity_id="entity_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/entities/entity_id/kyc", None, 1)


def test_kyc_create_entity_kyc() -> None:
    """Test createEntityKyc endpoint with WireMock"""
    test_id = "kyc.create_entity_kyc.0"
    client = get_client(test_id)
    client.kyc.create_entity_kyc(
        entity_id="entity_id",
        request=CreateKycInput_Baseline(
            data=BaselineKycCheckDataV0(
                country_code="SG",
                last_name="Doe",
                address_country_code="SG",
            ),
            provider_name="provider_name",
        ),
    )
    verify_request_count(test_id, "POST", "/api/v2/entities/entity_id/kyc", None, 1)


def test_kyc_create_entity_kyc_throws_unprocessable_entity_error() -> None:
    """Test createEntityKyc endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "kyc.create_entity_kyc.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.kyc.create_entity_kyc(
            entity_id="entity_id",
            request=CreateKycInput_Baseline(
                data=BaselineKycCheckDataV0(
                    country_code="xy",
                    last_name="x",
                    address_country_code="xy",
                ),
                provider_name="x",
            ),
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
    verify_request_count(test_id, "POST", "/api/v2/entities/entity_id/kyc", None, 1)


def test_kyc_get_entity_kyc_document() -> None:
    """Test getEntityKycDocument endpoint with WireMock"""
    test_id = "kyc.get_entity_kyc_document.0"
    client = get_client(test_id)
    client.kyc.get_entity_kyc_document(
        entity_id="entity_id",
        kyc_id="kyc_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/entities/entity_id/kyc/kyc_id/document", None, 1)


def test_kyc_create_entity_kyc_document() -> None:
    """Test createEntityKycDocument endpoint with WireMock"""
    test_id = "kyc.create_entity_kyc_document.0"
    client = get_client(test_id)
    client.kyc.create_entity_kyc_document(
        entity_id="entity_id",
        kyc_id="kyc_id",
        document_type="GOVERNMENT_ID",
        file="example_file",
    )
    verify_request_count(
        test_id, "POST", "/api/v2/entities/entity_id/kyc/kyc_id/document", {"document_type": "GOVERNMENT_ID"}, 1
    )


def test_kyc_create_managed_entity_kyc_embed() -> None:
    """Test createManagedEntityKycEmbed endpoint with WireMock"""
    test_id = "kyc.create_managed_entity_kyc_embed.0"
    client = get_client(test_id)
    client.kyc.create_managed_entity_kyc_embed(
        entity_id="entity_id",
    )
    verify_request_count(test_id, "POST", "/api/v2/entities/entity_id/kyc/url", None, 1)


def test_kyc_create_managed_entity_kyc_embed_throws_unprocessable_entity_error() -> None:
    """Test createManagedEntityKycEmbed endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "kyc.create_managed_entity_kyc_embed.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.kyc.create_managed_entity_kyc_embed(
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
    verify_request_count(test_id, "POST", "/api/v2/entities/entity_id/kyc/url", None, 1)
