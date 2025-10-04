from pydantic_settings import BaseSettings


class _Settings(BaseSettings):
     
     # auth
     SECRET_KEY: str
     ALGORITHM: str = 'HS256'
     ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

     # db
     MYSQL_DATABASE: str
     MYSQL_USER: str
     MYSQL_PASSWORD: str
     MYSQL_HOST: str
     MYSQL_PORT: str = 3306


     class Config:
          pass


settings = _Settings()
