from sqlalchemy import Column, BigInteger, String
from src.db.base import Base


class User(Base):
     __tablename__ = "users"

     id = Column(BigInteger, primary_key=True, index=True)
     email = Column(String, unique=True, index=True, nullable=False)
     hashed_password = Column(String, nullable=False)
     full_name = Column(String, nullable=False)
     is_active = Column(String, default=True)
