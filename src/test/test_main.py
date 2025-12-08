from fastapi.testclient import TestClient
from src.app.main import app


client = TestClient(app)


def test():
    assert 1 == 1
    assert 1 == 1