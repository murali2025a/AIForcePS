from fastapi.testclient import TestClient
from login_service.main import app
from login_service.database import Base, engine, SessionLocal

client = TestClient(app)

def test_register_api()
    response = client.post(
        register,
        params={username api_user, password 123, email api@test.com}
    )
    assert response.status_code == 200
    assert response.json()[message] == User registered

def test_login_api()
    # Register user first
    client.post(
        register,
        params={username login_user, password abc, email login@test.com}
    )

    response = client.post(
        login,
        params={username login_user, password abc}
    )

    assert response.status_code == 200
    assert response.json()[message] == Login successful
