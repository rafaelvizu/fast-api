from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.services import auth_service
from src.schemas.user import UserCreate, UserRead, UserLogin, Token

router = APIRouter(
     prefix='/api/auth',
     tags=['Auth'],
)

@router.post(
     '/register', 
     status_code=status.HTTP_201_CREATED,
     response_model=UserRead,
     name="Register"
)
def register(user: UserCreate, db: Session = Depends(get_db)) -> UserRead:
     user = auth_service.register_user(db=db, user=user)

     return user

@router.post(
     '/login', 
     status_code=status.HTTP_200_OK,
     response_model=Token,
     name="Login"
)
def login(user: UserLogin, db: Session = Depends(get_db)) -> Token:
     token = auth_service.login_user(db=db, user=user)

     return token