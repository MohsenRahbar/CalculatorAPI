"""API unit test (pytest)"""
import pytest
import fastapi
from Main import app  
from starlette.testclient import TestClient


client = TestClient(app)


def test_sum():
    """Tests successful addition using the '/calculate' endpoint."""
    response = client.post("/calculate", json={"num1": 2, "num2": 3, "operation": "sum"})
    assert response.status_code == 200  # Expect successful response
    assert response.json() == {"result": 5}  # Verify expected output


def test_division_by_zero():
    """Tests handling of division by zero with a custom error message."""
    response = client.post("/calculate", json={"num1": 10, "num2": 0, "operation": "division"})
    assert response.status_code == 400  # Expect bad request

    # More specific error message verification (assuming custom error handling)
    assert response.json()["detail"] == "Cannot divide by zero"
