from sqlalchemy.orm import (
    Session as _Session,
)
from src.models.user import (
    User as _User,
)
from src.core.security import (
    verify_password as _verify_password,
    get_password_hash as _get_password_hash,
    create_access_token as _create_access_token,
)
from src.exceptions.user_exceptions import (
    UserAlreadyExistsException as _UserAlreadyExistsException,
    UserNotFoundException as _UserNotFoundException,
    InvalidCredentialsException as _InvalidCredentialsException,
)
from src.schemas.user_schema import (
    UserCreate as _UserCreate,
    UserLogin as _UserLogin,
)

def authenticate_user(db: _Session, user: _UserLogin) -> _User:
    db_user = db.query(_User).filter(_User.email == user.email).first()
    if not db_user:
        raise _UserNotFoundException(user.email)

    if not _verify_password(user.password, db_user.hashed_password):
        raise _InvalidCredentialsException()

    return db_user

def register_user(db: _Session, user: _UserCreate) -> _User:
    # verificar se o usuário já existe
    existing_user = db.query(_User).filter(_User.email == user.email).first()
    if existing_user:
        raise _UserAlreadyExistsException(user.email)

    hashed_password = _get_password_hash(user.password)
    user = _User(
        email=user.email,
        hashed_password=hashed_password,
        full_name=user.full_name
    )
    db.add(user)
    db.commit()
    db.refresh(user)

    return user

def login_user(db: _Session, user: _UserLogin) -> str:
    user = authenticate_user(db, user)
    token = _create_access_token(data={"sub": str(user.id)})

    return token
