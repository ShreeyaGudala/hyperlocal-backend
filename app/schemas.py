from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    phone: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    phone: str

    class Config:
        orm_mode = True
