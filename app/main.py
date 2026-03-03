from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, auth
from .database import engine, SessionLocal, Base

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Hyperlocal Service Discovery API is running"}

@app.post("/signup", response_model=schemas.UserResponse)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
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
