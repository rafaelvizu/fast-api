from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.models.user import User
from src.services import auth_service
from src.schemas.user import UserCreate, UserRead, UserLogin, Token

router = APIRouter(
     prefix='/api/auth',
     tags=['Auth'],
)

@router.post('/register', status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)) -> UserRead:
     user = auth_service.register_user(db=db, user=user)

     return user

@router.post('/login', status_code=status.HTTP_200_OK)
def login(user: UserLogin, db: Session = Depends(get_db)) -> Token:
     user = auth_service.authenticate_user(db=db, user=user)
     token = auth_service.create_access_token(data={"sub": user.email})

     return Token(access_token=token, token_type="bearer")
