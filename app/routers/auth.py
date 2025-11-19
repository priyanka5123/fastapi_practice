from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.user_model import User
from app.security.hashing import hash_password, verify_password
from app.security.jwt_handler import create_access_token
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
router = APIRouter()

# Request schemas
class RegisterSchema(BaseModel):
    username: str
    password: str

class LoginSchema(BaseModel):
    username: str
    password: str

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Protected Route
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.get("/me")
def get_me(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        username = payload.get("sub")
        return {"username": username}
    except JWTError:
        raise HTTPException(401, "Invalid token")

# REGISTER
@router.post("/register")
def register_user(data: RegisterSchema, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == data.username).first()
    if existing:
        raise HTTPException(400, "Username already exists")

    user = User(
        username=data.username,
        password=hash_password(data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)
    return {"status": "user created"}


# LOGIN
@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == data.username).first()
    if not user:
        raise HTTPException(400, "Invalid username or password")

    if not verify_password(data.password, user.password):
        raise HTTPException(400, "Invalid username or password")

    token = create_access_token({"sub": user.username})

    return {"access_token": token, "token_type": "bearer"}
