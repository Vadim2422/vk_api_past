from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    username: str
    password: str


class User(UserBase):
    id: int
    username: str
    password: str

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    login: str
    password: str


class UserOut(UserBase):
    email: EmailStr
    username: str
    class Config:
        orm_mode = True