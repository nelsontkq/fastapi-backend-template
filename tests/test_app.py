from fastapi.testclient import TestClient
from unittest.mock import patch

import pytest

from api.main import app


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as client:
        yield client


@patch("api.util.settings.db_connection_string", "sqlite:///./db.sqlite3")
def test_youtube_valid_verify_token(client: TestClient):
    response = client.get("/users/1")
    assert response.status == 200
    assert response.json()["id"] == 1
