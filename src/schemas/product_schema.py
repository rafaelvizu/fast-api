from pydantic import BaseModel as _BaseModel, constr as _constr, Field as _Field
from typing import Annotated as _Annotated
from decimal import Decimal
from src.schemas import PaginationResponse as _PaginationResponse

_PositivePrice = _Annotated[
     Decimal,
     _Field(
          ge=0,
          description="Price must be a positive value",
          decimal_places=2,
          default=0.00
     )
]

class _ProductBase(_BaseModel):
    name: _constr(min_length=1, max_length=100, strip_whitespace=True)
    description: _constr(max_length=500, strip_whitespace=True) | None = None
    price: _PositivePrice

class ProductCreate(_ProductBase):
     pass

class ProductRead(_ProductBase):
     id: int
     user_id: int


     class Config:
          from_attributes = True

class ProductUpdate(_BaseModel):
     name: _constr(min_length=1, max_length=100, strip_whitespace=True) | None = None
     description: _constr(max_length=500, strip_whitespace=True) | None = None
     price: float | None = None

class ProductList(_BaseModel):
     products: list[ProductRead] = _Field(default_factory=list)
     pagination: _PaginationResponse = _Field(default_factory=_PaginationResponse)
     
     class Config:
          from_attributes = True