class User:
    def __init__(self, username, password, mfa_enabled=False):
        self.username = username
        self.password = password
        self.mfa_enabled = mfa_enabled
