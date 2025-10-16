from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_square():
    res = client.post("/square", json={"num": 5})
    assert res.status_code == 200
    assert res.json() == {"result": 25}


def test_square_get():
    res = client.get("/square/6")
    assert res.status_code == 200
    assert res.json() == {"result": 36}
