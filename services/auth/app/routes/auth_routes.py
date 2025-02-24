from fastapi import APIRouter, HTTPException, Depends
from app.security import get_password_hash, verify_password, create_access_token
from app.models import UserCreate, Token

auth_routes = APIRouter()

# Dummy user database (Replace with PostgreSQL later)
fake_users_db = {}

@auth_routes.post("/register")
def register(user: UserCreate):
    if user.email in fake_users_db:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    fake_users_db[user.email] = {"username": user.username, "email": user.email, "hashed_password": hashed_password}
    
    return {"message": "User registered successfully"}

@auth_routes.post("/login", response_model=Token)
def login(user: UserCreate):
    db_user = fake_users_db.get(user.email)
    if not db_user or not verify_password(user.password, db_user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}
