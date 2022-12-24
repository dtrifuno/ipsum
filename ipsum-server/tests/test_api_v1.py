from fastapi.testclient import TestClient

from ipsum_server.app import app

client = TestClient(app)

API_PREFIX = "/api/v1"


def test_health_check() -> None:
    """It returns an empty response with status code 200."""
    response = client.get(f"{API_PREFIX}/health_check")
    assert response.status_code == 200
    assert response.json() is None


def test_can_get_list_of_supported_languages() -> None:
    """It returns a list of objects describing the languages."""
    response = client.get(f"{API_PREFIX}/supported_languages")
    assert response.status_code == 200
    assert response.json().get("supported_languages") is not None


def test_can_generate_words() -> None:
    """It returns a list of words."""
    response = client.get(f"{API_PREFIX}/generate_words/en?count=50")
    assert response.status_code == 200
    assert len(response.json()) == 50


def test_can_generate_sentences() -> None:
    """It returns a list of sentences."""
    response = client.get(f"{API_PREFIX}/generate_sentences/en?count=10")
    assert response.status_code == 200
    assert len(response.json()) == 10


def test_can_generate_paragraphs() -> None:
    """It returns a list of paragraphs."""
    response = client.get(f"{API_PREFIX}/generate_paragraphs/en?count=5")
    assert response.status_code == 200


def test_cannot_ask_for_too_few_or_too_many_words() -> None:
    """It returns 422 Unprocessable Entity instead."""
    too_few = -1
    response = client.get(f"{API_PREFIX}/generate_words/en&count={too_few}")
    assert response.status_code == 422

    too_many = 10_000
    response = client.get(f"{API_PREFIX}/generate_words/en&count={too_many}")
    assert response.status_code == 422


def test_cannot_ask_for_too_few_or_too_many_sentences() -> None:
    """It returns 422 Unprocessable Entity instead."""
    too_few = -1
    response = client.get(f"{API_PREFIX}/generate_senteces/en&count={too_few}")

    too_many = 10_000
    response = client.get(f"{API_PREFIX}/generate_sentences/en&count={too_many}")
    assert response.status_code == 422


def test_cannot_ask_for_too_few_or_too_many_paragraphs() -> None:
    """It returns 422 Unprocessable Entity instead."""
    too_few = -1
    response = client.get(f"{API_PREFIX}/generate_paragraphs/en&count={too_few}")
    assert response.status_code == 422

    too_many = 10_000
    response = client.get(f"{API_PREFIX}/generate_paragraphs/en&count={too_many}")
    assert response.status_code == 422
