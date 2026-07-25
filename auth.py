from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from crud import create_user, get_user_by_email
from database import SessionLocal
from schemas import UserRegister
from security import create_access_token, verify_password

router = APIRouter()


@router.post("/register", status_code=status.HTTP_200_OK)
def register(user: UserRegister):
    db = SessionLocal()
    try:
        existing = get_user_by_email(db, str(user.email))
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")

        created_user = create_user(db, user)
        return {
            "message": "User Registered Successfully",
            "email": created_user.email,
            "role": created_user.role,
        }
    finally:
        db.close()


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    try:
        db_user = get_user_by_email(db, form_data.username)
        if not db_user:
            raise HTTPException(status_code=401, detail="Invalid Email")

        if not verify_password(form_data.password, db_user.password):
            raise HTTPException(status_code=401, detail="Wrong Password")

        token = create_access_token({"sub": db_user.email, "role": db_user.role})
        return {"access_token": token, "token_type": "bearer"}
    finally:
        db.close()