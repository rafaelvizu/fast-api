from pydantic import (
     BaseModel as _BaseModel, EmailStr as _EmailStr, Field as _Field, constr as _constr
)

class _UserBase(_BaseModel):
     email: _EmailStr
     full_name: _constr(min_length=1, max_length=100, strip_whitespace=True)


class UserCreate(_UserBase):
     password: _constr(min_length=6)

class UserLogin(_BaseModel):
     email: _EmailStr
     password: _constr(min_length=6)

class UserRead(_UserBase):
     id: int
     is_active: bool = _Field(default=True)

     class Config:
          from_attributes = True


class Token(_BaseModel):
     access_token: str
     token_type: str
     expires_in: float | None = None