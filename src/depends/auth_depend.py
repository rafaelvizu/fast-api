from fastapi import FastAPI, Request, Depends
from src.core.security import decode_access_token
from src.exceptions.http_execeptions import HTTPExceptions
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from src.models.user import User as _User
from sqlalchemy.orm import Session
from src.db.session import get_db


security = HTTPBearer()

def check_auth(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)) -> bool:
    # Example authentication logic
     token = credentials.credentials if credentials else None
     if token:
          try:
               decode = decode_access_token(token)
               user = db.query(_User).filter(_User.email == decode.get("sub")).first()
               if not user:
                    raise Exception("User not found")

               db.close()
               return True
          except Exception as e:
               db.close()
               return HTTPExceptions.unauthorized()
     else:
          db.close()
          return HTTPExceptions.unauthorized("Authorization header missing")

def get_current_user(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security), db: Session = Depends(get_db)) -> _User:
     token = credentials.credentials if credentials else None
     if token:
          try:
               decode = decode_access_token(token)
               print(decode)
               user = db.query(_User).filter(_User.id == decode.get("sub")).first()
               if not user:
                    raise Exception("User not found")

               db.close()
               return user
          except Exception as e:
               db.close()
               raise HTTPExceptions.unauthorized()
     else:
          db.close()
          raise HTTPExceptions.unauthorized("Authorization header missing")
     