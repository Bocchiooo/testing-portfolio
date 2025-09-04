import requests
import pytest

def test_JSONPlaceholder():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    responses = requests.get(url,timeout=10)
    assert responses.status_code == 200
    data = responses.json()
    assert data["id"] == 1
    assert "title" in data
