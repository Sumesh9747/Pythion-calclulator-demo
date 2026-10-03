import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_addition():
    client = app.test_client()

    response = client.post(
        "/",
        data={
            "num1": "10",
            "num2": "5",
            "operation": "add"
        }
    )

    assert b"15.0" in response.data
