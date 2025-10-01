from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.settings import settings

from src.db.base import Base
from src.models.user import User
from src.models.product import Product



DATABASE_URL = f"mysql+pymysql://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DATABASE}"


engine = create_engine(DATABASE_URL)

# criar todas as tabelas no banco de dados
Base.metadata.create_all(bind=engine)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
     db = SessionLocal()
     try:
          yield db
     finally:
          db.close()
