from fastapi import Request as _Request, Depends as _Depends
from src.core.security import decode_access_token as _decode_access_token
from src.exceptions.http_execeptions import HTTPExceptions as _HTTPExceptions
from fastapi.security import HTTPAuthorizationCredentials as _HTTPAuthorizationCredentials, HTTPBearer as _HTTPBearer
from src.models.user import User as _User
from sqlalchemy.orm import Session
from src.db.session import get_db


security = _HTTPBearer()

def check_auth(request: _Request, credentials: _HTTPAuthorizationCredentials = _Depends(security), db: Session = _Depends(get_db)) -> bool:
    # Example authentication logic
     token = credentials.credentials if credentials else None
     if token:
          try:
               decode = _decode_access_token(token)
               user = db.query(_User).filter(_User.email == decode.get("sub")).first()
               if not user:
                    raise Exception("User not found")

               db.close()
               return True
          except Exception as e:
               db.close()
               return _HTTPExceptions.unauthorized()
     else:
          db.close()
          return _HTTPExceptions.unauthorized("Authorization header missing")

def get_current_user(request: _Request, credentials: _HTTPAuthorizationCredentials = _Depends(security), db: Session = _Depends(get_db)) -> _User:
     token = credentials.credentials if credentials else None
     if token:
          try:
               decode = _decode_access_token(token)
               print(decode)
               user = db.query(_User).filter(_User.id == decode.get("sub")).first()
               if not user:
                    raise Exception("User not found")

               db.close()
               return user
          except Exception as e:
               db.close()
               raise _HTTPExceptions.unauthorized()
     else:
          db.close()
          raise _HTTPExceptions.unauthorized("Authorization header missing")
