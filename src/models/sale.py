from sqlalchemy import (
     Column as _Column, 
     BigInteger as _BigInteger, 
     DECIMAL as _DECIMAL, 
     ForeignKey as _ForeignKey, 
     UniqueConstraint as _UniqueConstraint,
     Enum as _Enum,
     DateTime as _DateTime,
     func as _func
)
from sqlalchemy.orm import relationship

from src.db.base import Base


class Sale(Base):
     __tablename__ = "sales"

     id = _Column(_BigInteger, primary_key=True, index=True)

     user_id = _Column(
          _BigInteger,
          _ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'),
          nullable=False,
     )
     discount = _Column(_DECIMAL(10, 2), nullable=False, default=0.00)

     total = _Column(_DECIMAL(10, 2), nullable=False)

     total_paid = _Column(_DECIMAL(10, 2), nullable=False)

     method_payment = _Column(
          _Enum('CASH', 'CREDIT_CARD', 'DEBIT_CARD', 'PIX', name='method_payment_enum'),
          nullable=False
     )

     status = _Column(
          _Enum('COMPLETED', 'CANCELLED', name='sale_status_enum'),
          nullable=False,
          default='COMPLETED'
     )
     
     created_at = _Column(_DateTime(timezone=True), server_default=_func.now(), nullable=False)
     updated_at = _Column(_DateTime(timezone=True), server_default=_func.now(), onupdate=_func.now(), nullable=False)

     __table_args__ = (
          _UniqueConstraint('user_id', 'id', name='uix_user_sale_id'),
     )

     user = relationship("User", back_populates="sales")
     items = relationship("SaleItem", back_populates="sale", cascade="all, delete-orphan")
