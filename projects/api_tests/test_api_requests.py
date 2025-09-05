import requests
import pytest
from projects.api_tests import dummy

BASE = "https://jsonplaceholder.typicode.com"

# 1. successful GET post/1
def test_get_post_success(monkeypatch):
    expected = {"id":1,"title":"title"}
    def fake_get(url, timeout=10):
        assert url.endswith("/posts/1")
        return dummy.DummyResponse(200, json_data=expected)
    monkeypatch.setattr(requests, "get", fake_get)
    r = requests.get(f"{BASE}/posts/1", timeout=10)
    assert r.status_code == 200
    assert r.json()["id"] == 1

# 2. GET not found -> 404
def test_get_post_not_found(monkeypatch):
    def fake_get(url, timeout=10):
        return dummy.DummyResponse(404, json_data={"error":"not found"})
    monkeypatch.setattr(requests, "get", fake_get)
    r = requests.get(f"{BASE}/posts/9999", timeout=10)
    assert r.status_code == 404

# 3. GET invalid JSON leads to exception
def test_get_invalid_json(monkeypatch):
    def fake_get(url, timeout=10):
        return dummy.DummyResponse(200, json_data=None, text_data="not json")
    monkeypatch.setattr(requests, "get", fake_get)
    r = requests.get(f"{BASE}/posts/1", timeout=10)
    with pytest.raises(ValueError):
        r.json()

# 4. POST create -> 201
def test_create_post_success(monkeypatch):
    payload = {"title":"a","body":"b","userId":1}
    def fake_post(url, json, timeout=10):
        assert url.endswith("/posts")
        assert json["title"] == "a"
        return dummy.DummyResponse(201, json_data={"id": 101, **json})
    monkeypatch.setattr(requests, "post", fake_post)
    r = requests.post(f"{BASE}/posts", json=payload, timeout=10)
    assert r.status_code == 201
    assert r.json()["id"] == 101

# 5. POST server error 500
def test_create_post_server_error(monkeypatch):
    def fake_post(url, json, timeout=10):
        return dummy.DummyResponse(500, json_data={"error":"server"})
    monkeypatch.setattr(requests, "post", fake_post)
    r = requests.post(f"{BASE}/posts", json={}, timeout=10)
    assert r.status_code == 500

# 6. PUT update success -> 200
def test_update_post_success(monkeypatch):
    payload = {"title":"updated"}
    def fake_put(url, json, timeout=10):
        assert url.endswith("/posts/1")
        return dummy.DummyResponse(200, json_data={"id":1, **json})
    monkeypatch.setattr(requests, "put", fake_put)
    r = requests.put(f"{BASE}/posts/1", json=payload, timeout=10)
    assert r.status_code == 200
    assert r.json()["title"] == "updated"

# 7. DELETE success -> 200 or 204
def test_delete_post_success(monkeypatch):
    def fake_delete(url, timeout=10):
        return dummy.DummyResponse(200, json_data={})
    monkeypatch.setattr(requests, "delete", fake_delete)
    r = requests.delete(f"{BASE}/posts/1", timeout=10)
    assert r.status_code in (200, 204)

# 8. Timeout raises requests.exceptions.Timeout
def test_get_timeout(monkeypatch):
    def fake_get(url, timeout=10):
        raise requests.exceptions.Timeout("timeout")
    monkeypatch.setattr(requests, "get", fake_get)
    with pytest.raises(requests.exceptions.Timeout):
        requests.get(f"{BASE}/posts/1", timeout=0.001)

# 9. Query param edge case: large id -> 404
def test_get_large_id_not_found(monkeypatch):
    def fake_get(url, timeout=10):
        # simulate that very large ids are not found
        return dummy.DummyResponse(404, json_data={"error":"not found"})
    monkeypatch.setattr(requests, "get", fake_get)
    r = requests.get(f"{BASE}/posts/123456789", timeout=10)
    assert r.status_code == 404

# 10. Validate headers sent (simulate service requiring header)
def test_get_requires_header(monkeypatch):
    def fake_get(url, timeout=10, headers=None):
        assert headers and headers.get("X-API-KEY") == "secret"
        return dummy.DummyResponse(200, json_data={"ok":True})
    monkeypatch.setattr(requests, "get", fake_get)
    r = requests.get(f"{BASE}/posts/1", timeout=10, headers={"X-API-KEY":"secret"})
    assert r.status_code == 200
