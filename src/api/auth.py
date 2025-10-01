from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.models.user import User
from src.services import auth_service
from src.core import settings

router = APIRouter(
     prefix='/api/auth',
     tags=['Auth'],
)

@router.post('/register', status_code=status.HTTP_201_CREATED)
def register(user: dict, db: Session = Depends(get_db)):
     pass