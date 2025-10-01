from pydantic import BaseModel, EmailStr, Field, constr

class UserBase(BaseModel):
     email: EmailStr
     full_name: constr(min_length=1, max_length=100, strip_whitespace=True)


class UserCreate(UserBase):
     password: constr(min_length=6)

class UserLogin(BaseModel):
     email: EmailStr
     password: constr(min_length=6)

class UserRead(UserBase):
     id: int
     is_active: bool = Field(default=True)

     class Config:
          from_attributes = True


class Token(BaseModel):
     access_token: str
     token_type: str
     expires_in: float | None = None