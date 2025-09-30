from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

from core.config import settings


oauth2_schema = OAuth2PasswordBearer(tokenUrl='/api/auth/login')

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
     return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
     return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
     to_encode = data.copy()
     expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
     to_encode.update({'exp': expire})
     
     return jwt.encode(
          to_encode,
          settings.SECRET_KEY,
          algorithm=settings.ALGORITHM,
     )

def decode_access_token(token: str = Depends(oauth2_schema)):
     credentials_exception = HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED,
          detail='Could not validate credentials',
          headers={'WWW-Authenticate': 'Bearer'},
     )
     try:
          payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
          username: str = payload.get('sub')

          if username is None:
               raise credentials_exception
          
          return payload
     except JWTError:
          raise credentials_exception