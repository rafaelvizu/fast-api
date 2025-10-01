from sqlalchemy.orm import Session
from src.models.user import User
from src.core.security import verify_password, get_password_hash, create_access_token
from src.exceptions.user import UserAlreadyExistsException, UserNotFoundException, InvalidCredentialsException

def authenticate_user(db: Session, username: str, password: str) -> User:
     user = db.query(User).filter(User.username == username).first()
     if not user:
          raise UserNotFoundException(username)
     
     if not verify_password(password, user.hashed_password):
          raise InvalidCredentialsException()
          
     return user

def register_user(db: Session, email: str, password: str, full_name: str) -> User:
     # verificar se o usuário já existe
     existing_user = db.query(User).filter(User.email == email).first()
     if existing_user:
          raise UserAlreadyExistsException(email)
     
     hashed_password = get_password_hash(password)
     user = User(
          email=email,
          hashed_password=hashed_password,
          full_name=full_name
     )
     db.add(user)
     db.commit()
     db.refresh(user)

     return user
     
def login_user(db: Session, username: str, password: str) -> str:
     user = authenticate_user(db, username, password)
     token = create_access_token(data={"sub": str(user.id)})
     return token