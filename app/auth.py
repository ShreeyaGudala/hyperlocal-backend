from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str):
    password = password.strip()
    password = password[:72]   # bcrypt limit safety
    return pwd_context.hash(password[:72])

def verify_password(plain_password: str, hashed_password: str):
    plain_password = plain_password.strip()
    plain_password = plain_password[:72]
    return pwd_context.verify(plain_password, hashed_password)
