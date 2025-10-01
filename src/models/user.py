from sqlalchemy import Column, BigInteger, String, VARCHAR
from src.db.base import Base


class User(Base):
     __tablename__ = "users"     

     id = Column(BigInteger, primary_key=True, index=True)
     email = Column(VARCHAR(100), unique=True, index=True, nullable=False)
     hashed_password = Column(VARCHAR(100), nullable=False)
     full_name = Column(VARCHAR(100), nullable=False)
     is_active = Column(VARCHAR(100), default=True)

