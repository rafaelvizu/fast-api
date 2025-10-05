from sqlalchemy import create_engine as _create_engine
from sqlalchemy.orm import sessionmaker as _sessionmaker
from src.core.settings import settings as _settings

from src.db.base import Base as _Base
from src.models.user import User as _User
from src.models.product import Product as _Product
from src.models.sale import Sale as _Sale
from src.models.sale_item import SaleItem as _SaleItem



DATABASE_URL = f"mysql+pymysql://{_settings.MYSQL_USER}:{_settings.MYSQL_PASSWORD}@{_settings.MYSQL_HOST}:{_settings.MYSQL_PORT}/{_settings.MYSQL_DATABASE}"


engine = _create_engine(DATABASE_URL)

# criar todas as tabelas no banco de dados
_Base.metadata.create_all(bind=engine)


_SessionLocal = _sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
     db = _SessionLocal()
     try:
          yield db
     finally:
          db.close()
