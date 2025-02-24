from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from app.models import User

SECRET_KEY = "72ba3ad5030f67b65c972e842825e424dc8c7ef4c703196af0514902c874eadf185cd29dddf8f1c9da0127b7f5a16f668ebca93de597424b72abaef655feac675c7b3bf52bab4a7c7467687fc93b837d1f53c575fc24d5e12e3f126049ba1f42300a5ec822f470300ffeda380e2941127454fa25fa018e02f34d021b87bc7e6572e5d18b137cb5fb39d3d0d97e2b8cd3546181fd671f5f9ca8394b9e81957440c6fe432498161a146c3b3173e9f9fa5e160d43811d9917e05a9bd0d382d4534f90a770c103469aa2cffee829a151003963061a6b35fca6a486c6e34f72c3892b655d37a6181d1687fc42f4002e96e8f71d630ab421c1971a0a0bb974cba40c7d"  # Replace with a secure secret key
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
