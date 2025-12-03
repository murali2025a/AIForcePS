from login_service.auth_dao import AuthDAO
from login_service.models import User

def test_create_user(db_session):
    dao = AuthDAO(db_session)

    user = dao.create_user("john", "pass123", "john@example.com")

    assert user.username == "john"
    assert user.email == "john@example.com"

def test_get_user_by_username(db_session):
    dao = AuthDAO(db_session)
    dao.create_user("mary", "abc123", "mary@example.com")

    user = dao.get_user_by_username("mary")

    assert user is not None
    assert user.username == "mary"

def test_validate_credentials(db_session):
    dao = AuthDAO(db_session)
    dao.create_user("sam", "mypw", "sam@example.com")

    user = dao.validate_credentials("sam", "mypw")

    assert user is not None
