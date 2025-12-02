from sqlalchemy.orm import Session
from .models import User

class AuthDAO:

    def __init__(self, db: Session):
        self.db = db

    def get_user_by_username(self, username: str):
        return self.db.query(User).filter(User.username == username).first()

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, username: str, password: str, email: str):
        new_user = User(username=username, password=password, email=email)
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user

    def validate_credentials(self, username: str, password: str):
        return self.db.query(User).filter(
            User.username == username,
            User.password == password
        ).first()

    def user_exists(self, username: str) -> bool:
        return self.db.query(User).filter(User.username == username).first() is not None
