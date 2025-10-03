from sqlalchemy import Column, BigInteger, VARCHAR
from src.db.base import Base
from sqlalchemy.orm import relationship


class User(Base):
     __tablename__ = "users"     

     id = Column(BigInteger, primary_key=True, index=True)
     email = Column(VARCHAR(100), unique=True, index=True, nullable=False)
     hashed_password = Column(VARCHAR(100), nullable=False)
     full_name = Column(VARCHAR(100), nullable=False)
     is_active = Column(VARCHAR(100), default=True)

     products = relationship("Product", back_populates="user", cascade="all, delete-orphan")

