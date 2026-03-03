from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    phone: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    phone: str

    class Config:
        from_attributes = True
