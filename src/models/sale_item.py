from sqlalchemy import (
     Column as _Column, 
     BigInteger as _BigInteger, 
     DECIMAL as _DECIMAL, 
     INTEGER as _INTEGER,
     ForeignKey as _ForeignKey, 
     UniqueConstraint as _UniqueConstraint,
     DateTime as _DateTime,
     func as _func
)
from sqlalchemy.orm import relationship

from src.db.base import Base


class SaleItem(Base):
     __tablename__ = "sales_items"

     id = _Column(_BigInteger, primary_key=True, index=True)

     sale_id = _Column(
          _BigInteger,
          _ForeignKey('sales.id', ondelete='CASCADE', onupdate='CASCADE'),
          nullable=False,
     )

     product_id = _Column(
          _BigInteger,
          _ForeignKey('products.id', ondelete='CASCADE', onupdate='CASCADE'),
          nullable=False,
     )

     quantity = _Column(
          _INTEGER,
          nullable=False,
     )

     price = _Column(_DECIMAL(10, 2), nullable=False)
     total = _Column(_DECIMAL(10, 2), nullable=False)

     created_at = _Column(_DateTime(timezone=True), server_default=_func.now(), nullable=False)
     updated_at = _Column(_DateTime(timezone=True), server_default=_func.now(), onupdate=_func.now(), nullable=False)

     __table_args__ = (
          _UniqueConstraint('sale_id', 'product_id', name='uix_sale_product_id'),
     )

     sale = relationship("Sale", back_populates="itens")
     product = relationship("Product", back_populates="itens")
