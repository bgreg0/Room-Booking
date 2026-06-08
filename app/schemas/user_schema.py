from uuid import UUID
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: UUID

    class Config:
        from_attributes = True
