from app import app
import pytest
def test_index():
    tester=app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Financial Agent Pro" in response.data