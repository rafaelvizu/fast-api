from sqlalchemy import (
     Column as _Column, BigInteger as _BigInteger, VARCHAR as _VARCHAR, TEXT as _TEXT, DECIMAL as _DECIMAL, ForeignKey as _ForeignKey, UniqueConstraint as _UniqueConstraint
)
from sqlalchemy.orm import relationship
from src.db.base import Base


class Product(Base):
     __tablename__ = "products"     

     id = _Column(_BigInteger, primary_key=True, index=True)
     user_id = _Column(
          _BigInteger, 
          _ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'), 
          nullable=False,
     )

     name = _Column(_VARCHAR(100), nullable=False)
     description = _Column(_TEXT, nullable=True)
     price = _Column(_DECIMAL(10, 2), nullable=False)

     __table_args__ = (
          _UniqueConstraint('user_id', 'name', name='uix_user_product_name'),
     )

     user = relationship("User", back_populates="products")
