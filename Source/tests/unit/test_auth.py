from backend.services.auth_service import AuthService

def test_validate_user():
    service = AuthService()
    user = service.validate_user("test", "pass")
    assert user.username == "test"

def test_generate_otp():
    service = AuthService()
    user = type("User", (), {"username": "test"})()
    otp = service.generate_otp(user)
    assert 100000 <= otp <= 999999
