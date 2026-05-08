from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from fastapi.security import OAuth2PasswordRequestForm

from app.schemas.auth import (
    Register,
    Login,
    ForgotPassword,
    ResetPassword
)

from app.services.auth_service import (
    register_user,
    login_user,
    forgot_password,
    reset_password
)
router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    data: Register,
    db: Session = Depends(get_db)
):

    return register_user(db, data)






@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    return login_user(db, form_data)

@router.post("/forgot-password")
def forgot_password_api(
    data: ForgotPassword,
    db: Session = Depends(get_db)
):

    return forgot_password(
        db,
        data
    )



@router.post("/reset-password")
def reset_password_api(
    data: ResetPassword,
    db: Session = Depends(get_db)
):

    return reset_password(
        db,
        data
    )