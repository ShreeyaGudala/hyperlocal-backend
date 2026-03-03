from pydantic import BaseModel, EmailStr, Field
from typing import Optional


# =========================
# Base Schema (Shared Fields)
# =========================

class UserBase(BaseModel):
    email: EmailStr


# =========================
# Create User (Signup)
# =========================

class UserCreate(UserBase):
    password: str = Field(
        ...,
        min_length=6,
        max_length=72
    )


# =========================
# User Response (Return to Client)
# =========================

class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # for SQLAlchemy ORM (Pydantic v2)


# =========================
# Login Schema (Optional but Recommended)
# =========================

class UserLogin(BaseModel):
    email: EmailStr
    password: str
