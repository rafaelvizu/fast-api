from pydantic_settings import BaseSettings


class Settings(BaseSettings):
     
     # auth
     SECRET_KEY: str
     ALGORITHM: str = 'HS256'
     ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

     # db
     MYSQL_DATABASE: str
     MYSQL_USER: str
     MYSQL_PASSWORD: str
     MYSQL_HOST: str
     MYSQL_PORT: int = 3306


     class Config:
          env_file = '.env'


settings = Settings()
