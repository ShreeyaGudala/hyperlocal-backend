from pydantic import BaseModel, EmailStr, Field


# ==========================
# Base User Schema
# ==========================
class UserBase(BaseModel):
    email: EmailStr


# ==========================
# Signup Schema (Request Body)
# ==========================
class UserCreate(UserBase):
    password: str = Field(
        ...,
        min_length=6,
        max_length=72
    )


# ==========================
# User Response Schema (Returned to Client)
# ==========================
class UserResponse(UserBase):
    id: int

    class Config:
        from_attributes = True  # Required for SQLAlchemy ORM
