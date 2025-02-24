from sqlalchemy import Column, Integer, String, Boolean
from app.config import Base
from pydantic import BaseModel
from typing import Optional

# SQLAlchemy User Model (Database Table)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

# Pydantic Schemas (For Request Validation)
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
