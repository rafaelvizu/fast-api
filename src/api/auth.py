from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.services import auth_service
from src.schemas.user import UserCreate, UserRead, UserLogin, Token
from src.schemas import Message
from src.exceptions.user import UserAlreadyExistsException, UserNotFoundException, InvalidCredentialsException
from fastapi.responses import JSONResponse

router = APIRouter(
     prefix='/api/auth',
     tags=['Auth'],
)

@router.post(
     '/register', 
     status_code=status.HTTP_201_CREATED,
     response_model=UserRead,
     name="Register",
     responses={
          400: {"description": UserAlreadyExistsException.__doc__},
          500: {"description": "Internal server error"},
     }
)
def register(user: UserCreate, db: Session = Depends(get_db)) -> UserRead | JSONResponse:
     try:
          return auth_service.register_user(db=db, user=user)
     
     except UserAlreadyExistsException as e:
          return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": str(e)})
     
     except Exception as e:
          return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "Internal server error"})
     
@router.post(
     '/login', 
     status_code=status.HTTP_200_OK,
     response_model=Token,
     name="Login",
     responses={
          401: {"model": Message, "description": "Unauthorized - Invalid credentials"},
          500: {"model": Message, "description": "Internal server error"},
     }
)
def login(user: UserLogin, db: Session = Depends(get_db)) -> Token | JSONResponse:
     try:
          return auth_service.login_user(db=db, user=user)
          
     except (UserNotFoundException, InvalidCredentialsException) as e:
          return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"message": str(e)})
     
     except Exception as e:
          return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "Internal server error"})
