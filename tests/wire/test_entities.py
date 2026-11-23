import pytest
from .conftest import get_client, verify_request_count

from dinari_api_sdk import UnprocessableEntityError
from dinari_api_sdk.core.jsonable_encoder import jsonable_encoder


def test_entities_get_entities() -> None:
    """Test getEntities endpoint with WireMock"""
    test_id = "entities.get_entities.0"
    client = get_client(test_id)
    client.entities.get_entities()
    verify_request_count(test_id, "GET", "/api/v2/entities/", None, 1)


def test_entities_get_entities_throws_unprocessable_entity_error() -> None:
    """Test getEntities endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "entities.get_entities.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.entities.get_entities()
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
    verify_request_count(test_id, "GET", "/api/v2/entities/", None, 1)


def test_entities_create_entities() -> None:
    """Test createEntities endpoint with WireMock"""
    test_id = "entities.create_entities.0"
    client = get_client(test_id)
    client.entities.create_entities(
        name="name",
    )
    verify_request_count(test_id, "POST", "/api/v2/entities/", None, 1)


def test_entities_create_entities_throws_unprocessable_entity_error() -> None:
    """Test createEntities endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "entities.create_entities.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.entities.create_entities(
            name="x",
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
    verify_request_count(test_id, "POST", "/api/v2/entities/", None, 1)


def test_entities_get_current_entity() -> None:
    """Test getCurrentEntity endpoint with WireMock"""
    test_id = "entities.get_current_entity.0"
    client = get_client(test_id)
    client.entities.get_current_entity()
    verify_request_count(test_id, "GET", "/api/v2/entities/me", None, 1)


def test_entities_get_entity_by_id() -> None:
    """Test getEntityById endpoint with WireMock"""
    test_id = "entities.get_entity_by_id.0"
    client = get_client(test_id)
    client.entities.get_entity_by_id(
        entity_id="entity_id",
    )
    verify_request_count(test_id, "GET", "/api/v2/entities/entity_id", None, 1)


def test_entities_update_entity_by_id() -> None:
    """Test updateEntityById endpoint with WireMock"""
    test_id = "entities.update_entity_by_id.0"
    client = get_client(test_id)
    client.entities.update_entity_by_id(
        entity_id="entity_id",
    )
    verify_request_count(test_id, "PATCH", "/api/v2/entities/entity_id", None, 1)


def test_entities_update_entity_by_id_throws_unprocessable_entity_error() -> None:
    """Test updateEntityById endpoint error response (UnprocessableEntityError) with WireMock"""
    test_id = "entities.update_entity_by_id.1"
    client = get_client(test_id)
    with pytest.raises(UnprocessableEntityError) as exc_info:
        client.entities.update_entity_by_id(
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
    verify_request_count(test_id, "PATCH", "/api/v2/entities/entity_id", None, 1)
