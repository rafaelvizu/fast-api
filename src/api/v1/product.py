from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.services import auth_service
from src.schemas import Message
from fastapi.responses import JSONResponse
from src.depends.auth_depend import check_auth



router = APIRouter(
     prefix='/api/v1/product',
     tags=['Product'],
)

@router.get(
     '/',
     status_code=status.HTTP_200_OK,
     name="Get Products",
     dependencies=[Depends(check_auth)],
     responses={
          401: {"model": Message, "description": "Unauthorized - Invalid credentials"},
          500: {"model": Message, "description": "Internal server error"},
     }
)
def get_products(db: Session = Depends(get_db)) -> dict:
     # teste
     return {"products": ["Product 1", "Product 2", "Product 3"]}