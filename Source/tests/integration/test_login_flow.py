def test_login_flow_with_mfa():
    # Simulate login + otp verification
    from backend.controllers.auth_controller import AuthController
    controller = AuthController()
    login_res = controller.login("user", "pass")
    assert login_res["status"] == "MFA_REQUIRED"
    otp_res = controller.verify_otp("user", 123456)
    assert otp_res == True
