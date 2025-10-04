from sqlalchemy.orm import Session as _Session
from src.models.product import Product as _Product
from src.exceptions.product_exceptions import (
     ProductNotFoundException,
     ProductAlreadyExistsException,
)
from src.schemas import PaginationResponse as _PaginationResponse
from typing import List


def get_product(db: _Session, product_id: int) -> _Product:
    product = db.query(_Product).filter(_Product.id == product_id).first()
    if not product:
        raise ProductNotFoundException(product_id)
    
    return product

def create_product(db: _Session, name: str, description: str, price: float, user_id: str) -> _Product:
     existing_product = db.query(_Product).filter(_Product.name == name, _Product.user_id == user_id).first()
     
     if existing_product:
          raise ProductAlreadyExistsException(name)
    
     product = _Product(name=name, description=description, price=price, user_id=user_id)
     db.add(product)
     db.commit()
     db.refresh(product)
     return product

def get_all_products(db: _Session, page: int = 1, page_size: int = 10) -> tuple[_PaginationResponse, List[_Product]]:
     offset = (page - 1) * page_size

     pagination: _PaginationResponse = _PaginationResponse(
          page=page,
          size=page_size,
          total=db.query(_Product).count(),
          total_pages=(db.query(_Product).count() + page_size - 1) // page_size,
          has_next=db.query(_Product).count() > page * page_size
     )
     
     products = db.query(_Product).offset(offset).limit(page_size).all()
     return pagination, products

def edit_product(db: _Session, product_id: int, user_id: int, name: str = None, description: str = None, price: float = None) -> _Product:
     product = db.query(_Product).filter(_Product.id == product_id, _Product.user_id == user_id).first()
     if not product:
          raise ProductNotFoundException(product_id)
     if name is not None:
          product_exists = db.query(_Product).filter(_Product.name == name, _Product.user_id == user_id, _Product.id != product_id).first()
          if product_exists:
               raise ProductAlreadyExistsException(name)
          
          product.name = name
     if description is not None:
          product.description = description
     if price is not None:
          product.price = price
     
     db.commit()
     db.refresh(product)
     return product


def delete_product(db: _Session, product_id: int, user_id: int) -> bool:
     product = db.query(_Product).filter(_Product.id == product_id, _Product.user_id == user_id).first()

     if not product:
          raise ProductNotFoundException(product_id)
     
     db.delete(product)
     db.commit()
     return True
