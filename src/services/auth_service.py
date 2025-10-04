from sqlalchemy.orm import Session
from src.models.user import User
from src.core.security import verify_password, get_password_hash, create_access_token
from exceptions.user_exceptions import UserAlreadyExistsException, UserNotFoundException, InvalidCredentialsException
from schemas.user_schema import UserCreate, UserLogin, UserRead

def authenticate_user(db: Session, user: UserLogin) -> User:
     db_user = db.query(User).filter(User.email == user.email).first()
     if not db_user:
          raise UserNotFoundException(user.email)

     if not verify_password(user.password, db_user.hashed_password):
          raise InvalidCredentialsException()

     return db_user

def register_user(db: Session, user: UserCreate) -> User:
     # verificar se o usuário já existe
     existing_user = db.query(User).filter(User.email == user.email).first()
     if existing_user:
          raise UserAlreadyExistsException(user.email)

     hashed_password = get_password_hash(user.password)
     user = User(
          email=user.email,
          hashed_password=hashed_password,
          full_name=user.full_name
     )
     db.add(user)
     db.commit()
     db.refresh(user)

     return user

def login_user(db: Session, user: UserLogin) -> str:
     user = authenticate_user(db, user)
     token = create_access_token(data={"sub": str(user.id)})

     return token
