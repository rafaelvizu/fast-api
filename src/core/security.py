from datetime import datetime as _datetime, timedelta as _timedelta
from jose import JWTError as _JWTError, jwt as _jwt
from fastapi import Depends as _Depends 
from fastapi.security import OAuth2PasswordBearer as _OAuth2PasswordBearer
from passlib.context import CryptContext as _CryptContext
from src.exceptions.http_execeptions import HTTPExceptions as _HTTPExceptions

from src.core.settings import settings as _settings


_oauth2_schema = _OAuth2PasswordBearer(tokenUrl='/api/auth/login')

_pwd_context = _CryptContext(schemes=['bcrypt'], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
     return _pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
     return _pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: _timedelta | None = None) -> dict:
     to_encode = data.copy()
     expire = _datetime.utcnow() + (expires_delta or _timedelta(minutes=_settings.ACCESS_TOKEN_EXPIRE_MINUTES))
     to_encode.update({'exp': expire})
     
     return {
          'access_token': _jwt.encode(to_encode, _settings.SECRET_KEY, algorithm=_settings.ALGORITHM),
          'token_type': 'bearer',
          'expires_in': expire.timestamp()
     }

def decode_access_token(token: str = _Depends(_oauth2_schema)):

     try:
          payload = _jwt.decode(token, _settings.SECRET_KEY, algorithms=[_settings.ALGORITHM])
          username: str = payload.get('sub')

          if username is None:
               raise _HTTPExceptions.unauthorized()
          
          return payload
     except _JWTError:
          raise _HTTPExceptions.unauthorized()
