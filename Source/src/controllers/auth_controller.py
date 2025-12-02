from services.auth_service import AuthService

class AuthController:
    def __init__(self):
        self.auth_service = AuthService()

    def login(self, username, password):
        user = self.auth_service.validate_user(username, password)
        if user and user.mfa_enabled:
            otp = self.auth_service.generate_otp(user)
            return {"status": "MFA_REQUIRED", "otp_sent": True}
        elif user:
            return {"status": "SUCCESS"}
        else:
            return {"status": "FAILURE"}

    def verify_otp(self, username, otp):
        return self.auth_service.verify_otp(username, otp)
