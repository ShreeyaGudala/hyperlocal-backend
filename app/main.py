from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas, auth
from .database import engine, get_db, Base

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Hyperlocal Backend Running"}

@app.post("/signup", response_model=schemas.UserResponse, status_code=status.HTTP_201_CREATED)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):

    # Check duplicate email
    existing_user = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    hashed_pw = auth.hash_password(user.password)

    new_user = models.User(
        email=user.email,
        phone=user.phone,
        hashed_password=hashed_pw
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
@app.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        return {"database": "connected"}
    except Exception as e:
        return {"error": str(e)}
