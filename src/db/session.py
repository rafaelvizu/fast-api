from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.config import settings


DATABASE_URL = f"mysql+pymysql://{settings.MYSQL_USER}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DATABASE}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
     db = SessionLocal()
     try:
          yield db
     finally:
          db.close()
