# capstone/tests/test_service.py

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch

# Add the project root to the Python path to allow for absolute imports
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.service import app

# Initialize the test client
client = TestClient(app)

# --- Unit Tests for the API Endpoints ---

def test_health_check():
    """
    Test the /health endpoint to ensure it's working correctly.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

@patch('src.service.infer')
def test_get_recommendations_success(mock_infer):
    """
    Test the /recommendations endpoint for a successful request.
    The 'infer' function is mocked to isolate the service logic.
    """
    # Configure the mock to return a predictable result
    mock_response = {
        "user_id": "user-123",
        "recommendations": ["item_10", "item_20"],
        "confidence": 0.92
    }
    mock_infer.return_value = mock_response

    # Make the request to the endpoint
    request_data = {"user_id": "user-123", "context": {"source": "test"}}
    response = client.post("/recommendations", json=request_data)

    # Assertions
    assert response.status_code == 200
    assert response.json() == mock_response
    mock_infer.assert_called_once_with({"user_id": "user-123", "context": {"source": "test"}})

def test_get_recommendations_invalid_input():
    """
    Test the /recommendations endpoint with a missing 'user_id'.
    This should result in a 422 Unprocessable Entity error from FastAPI's validation.
    """
    # Make a request with an invalid payload
    request_data = {"context": {}} # Missing user_id
    response = client.post("/recommendations", json=request_data)

    # Assertions
    assert response.status_code == 422 # FastAPI's validation error

@patch('src.service.infer')
def test_get_recommendations_internal_error(mock_infer):
    """
    Test the /recommendations endpoint for an internal server error.
    The 'infer' function is mocked to raise an exception.
    """
    # Configure the mock to raise an exception
    mock_infer.side_effect = Exception("ML model failure")

    # Make the request
    request_data = {"user_id": "user-456"}
    response = client.post("/recommendations", json=request_data)

    # Assertions
    assert response.status_code == 500
    assert "An internal error occurred" in response.json()["detail"]
