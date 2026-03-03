from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, auth
from .database import engine, get_db, Base

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)


# -----------------------
# Root Endpoint
# -----------------------
@app.get("/")
def root():
    return {"message": "Hyperlocal Backend Running"}


# -----------------------
# Signup Endpoint
# -----------------------
@app.post("/signup", response_model=schemas.UserResponse)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # Check if user already exists
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Hash password (bcrypt safe)
    hashed_password = auth.hash_password(user.password)

    # Create user
    new_user = models.User(
        email=user.email,
        hashed_password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
