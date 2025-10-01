from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.services import auth_service
from src.schemas import Message
from fastapi.responses import JSONResponse

router = APIRouter(
     prefix='/api/v1/product',
     tags=['Product'],
)
