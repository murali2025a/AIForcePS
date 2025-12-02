from sqlalchemy.orm import Session
from .auth_dao import AuthDAO

class AuthService:

    def __init__(self, db: Session):
        self.dao = AuthDAO(db)

    def login(self, username: str, password: str):
        user = self.dao.validate_credentials(username, password)
        if not user:
            raise Exception("Invalid username or password")
        if not user.active:
            raise Exception("User account is inactive")
        return user

    def register(self, username: str, password: str, email: str):
        if self.dao.user_exists(username):
            raise Exception("Username already taken")
        return self.dao.create_user(username, password, email)

    def get_user(self, username: str):
        return self.dao.get_user_by_username(username)
