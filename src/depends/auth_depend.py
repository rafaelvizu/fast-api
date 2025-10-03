from fastapi import FastAPI, Request, Depends
from src.core.security import decode_access_token
from src.exceptions.http_execeptions import HTTPExceptions
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer


security = HTTPBearer()

async def check_auth(request: Request, credentials: HTTPAuthorizationCredentials = Depends(security)) -> bool:
    # Example authentication logic
     token = credentials.credentials if credentials else None
     if token:
          try:
               decode_access_token(token)
          except Exception as e:
               return HTTPExceptions.unauthorized()
     else:
          return HTTPExceptions.unauthorized("Authorization header missing")

     return True