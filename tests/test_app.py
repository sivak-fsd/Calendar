import pytest
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_index(client):
    res = client.get("/")
    assert res.status_code == 200


def test_get_calendar(client):
    res = client.get("/api/calendar/2026/4")
    assert res.status_code == 200
    data = res.get_json()
    assert data["month_name"] == "April"
    assert data["year"] == 2026
    assert len(data["weeks"]) > 0
