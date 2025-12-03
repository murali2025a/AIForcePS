import pytest
from login_service.auth_service import AuthService
from login_service.auth_dao import AuthDAO

def test_register_user(db_session):
    service = AuthService(db_session)

    user = service.register("alice", "xyz123", "alice@test.com")

    assert user.username == "alice"
    assert user.email == "alice@test.com"

def test_register_existing_user(db_session):
    service = AuthService(db_session)
    service.register("bob", "pass", "bob@test.com")

    with pytest.raises(Exception):
        service.register("bob", "pass", "bob@test.com")

def test_login_success(db_session):
    service = AuthService(db_session)
    service.register("mark", "111", "mark@test.com")

    user = service.login("mark", "111")

    assert user.username == "mark"

def test_login_invalid_credentials(db_session):
    service = AuthService(db_session)
    service.register("lucy", "222", "lucy@test.com")

    with pytest.raises(Exception):
        service.login("lucy", "wrongpassword")
