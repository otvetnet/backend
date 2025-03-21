from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str
    age: int


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int