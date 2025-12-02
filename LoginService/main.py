from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import Base, engine, SessionLocal
from .auth_service import AuthService

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    service = AuthService(db)
    user = service.login(username, password)
    return {"message": "Login successful", "user_id": user.id}

@app.post("/register")
def register(username: str, password: str, email: str, db: Session = Depends(get_db)):
    service = AuthService(db)
    user = service.register(username, password, email)
    return {"message": "User registered", "user_id": user.id}
