from sqlalchemy import Column, BigInteger, VARCHAR, TEXT, DECIMAL, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from src.db.base import Base


class Product(Base):
     __tablename__ = "products"     

     id = Column(BigInteger, primary_key=True, index=True)
     user_id = Column(
          BigInteger, 
          ForeignKey('users.id', ondelete='CASCADE', onupdate='CASCADE'), 
          nullable=False,
     )

     name = Column(VARCHAR(100), nullable=False)
     description = Column(TEXT, nullable=True)
     price = Column(DECIMAL(10, 2), nullable=False)

     __table_args__ = (
          UniqueConstraint('user_id', 'name', name='uix_user_product_name'),
     )

     user = relationship("User", back_populates="products")
