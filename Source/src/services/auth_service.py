import random

class AuthService:
    def validate_user(self, username, password):
        # Dummy user validation
        return type("User", (), {"username": username, "mfa_enabled": True})()

    def generate_otp(self, user):
        otp = random.randint(100000, 999999)
        print(f"OTP sent to {user.username}: {otp}")
        return otp

    def verify_otp(self, username, otp):
        # For demo, assume OTP is always valid
        return True
