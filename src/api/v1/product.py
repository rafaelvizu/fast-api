from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.schemas import Message
from fastapi.responses import JSONResponse
from src.depends.auth_depend import (
     check_auth,
     get_current_user,
)
from src.models.user import User
from src.services.product_service import (
     create_product,
     get_product,
     get_all_products,
     edit_product,
     delete_product
)
from src.schemas.product_schema import (
     ProductCreate,
     ProductRead,
     ProductUpdate,
     ProductList
)
from src.schemas import (
     PaginationRequest,
)
from src.exceptions.product_exceptions import (
     ProductNotFoundException,
     ProductAlreadyExistsException,
)


router = APIRouter(
     prefix='/api/v1/product',
     tags=['Product'],
     dependencies=[Depends(check_auth)],
     responses={
          401: {"model": Message, "description": "Unauthorized - Invalid credentials"},
          404: {"model": Message, "description": "Product not found"},
          500: {"model": Message, "description": "Internal server error"},
     }
)

@router.get(
     '/',
     status_code=status.HTTP_200_OK,
     name="Get Products",
     response_model=ProductList,
)
def get_all(db: Session = Depends(get_db), pagination_request: PaginationRequest = Depends(), user: User = Depends(get_current_user)) -> ProductList:
     pagination_res, products = get_all_products(db, user.id, pagination_request.page, pagination_request.size)

     return ProductList(products=products, pagination=pagination_res)


@router.get(
     '/{product_id}',
     status_code=status.HTTP_200_OK,
     name="Get Product by ID",
)

def get_by_id(product_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> ProductRead:
     try:
          product = get_product(db, product_id, user.id)
          return product
     except ProductNotFoundException as e:
          return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": str(e)})
     except Exception as e:
          return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "Internal server error"})

@router.post(
     '/',
     status_code=status.HTTP_201_CREATED,
     name="Create Product",
     response_model=ProductRead,
)
def create(product: ProductCreate, db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> ProductRead:
     try:
          created_product = create_product(db, product.name, product.description, product.price, user.id)
          return created_product
     except ProductAlreadyExistsException as e:
          return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": str(e)})
     except Exception as e:
          return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "Internal server error"})

@router.put(
     '/{product_id}',
     status_code=status.HTTP_200_OK,
     name="Edit Product",
     response_model=ProductRead,
)

def update(product_id: int, product: ProductUpdate, db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> ProductRead:
     try:
          updated_product = edit_product(db, product_id, user.id, product.name, product.description, product.price)
          return updated_product
     except ProductNotFoundException as e:
          return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": str(e)})
     except Exception as e:
          return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "Internal server error"})

@router.delete(
     '/{product_id}',
     status_code=status.HTTP_200_OK,
     name="Delete Product",
     responses={
          401: {"model": Message, "description": "Unauthorized - Invalid credentials"},
          404: {"model": Message, "description": "Product not found"},
          500: {"model": Message, "description": "Internal server error"},
     }
)
def delete(product_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)) -> Message:
     try:
          delete_product(db, product_id, user.id)
          return Message(message="Product deleted successfully")
     except ProductNotFoundException as e:
          return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": str(e)})
     except Exception as e:
          return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "Internal server error"})
