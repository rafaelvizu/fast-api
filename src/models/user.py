from sqlalchemy import (
     Column as _Column, BigInteger as _BigInteger, VARCHAR as _VARCHAR
)
from src.db.base import Base
from sqlalchemy.orm import relationship


class User(Base):
     __tablename__ = "users"     

     id = _Column(_BigInteger, primary_key=True, index=True)
     email = _Column(_VARCHAR(100), unique=True, index=True, nullable=False)
     hashed_password = _Column(_VARCHAR(100), nullable=False)
     full_name = _Column(_VARCHAR(100), nullable=False)
     is_active = _Column(_VARCHAR(100), default=True)

     products = relationship("Product", back_populates="user", cascade="all, delete-orphan")

