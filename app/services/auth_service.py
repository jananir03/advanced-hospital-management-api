from sqlalchemy.orm import Session
from fastapi import HTTPException
import uuid

from app.models.user import User

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)


def register_user(db: Session, data):

    existing_user = db.query(User).filter(
        User.username == data.username
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    hashed_password = hash_password(data.password)

    user = User(
        username=data.username,
        email=data.email,
        password=hashed_password,
        role=data.role
    )

    db.add(user)

    db.commit()

    db.refresh(user)

    return {
        "message": "User registered successfully"
    }



def login_user(db: Session, data):

    user = db.query(User).filter(
        User.username == data.username
    ).first()

    if not user:
        raise HTTPException(
            status_code=400,
            detail="Invalid username"
        )

    if not verify_password(
        data.password,
        user.password
    ):
        raise HTTPException(
            status_code=400,
            detail="Invalid password"
        )

    access_token = create_access_token({
        "user_id": user.id,
        "role": user.role
    })

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

def forgot_password(
    db,
    data
):

    user = db.query(User).filter(
        User.username == data.username
    ).first()

    if not user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    token = str(uuid.uuid4())

    user.reset_token = token

    db.commit()

    return {
        "message": "Reset token generated",
        "reset_token": token
    }



def reset_password(
    db,
    data
):

    user = db.query(User).filter(
        User.reset_token == data.token
    ).first()

    if not user:

        raise HTTPException(
            status_code=400,
            detail="Invalid token"
        )

    user.password = hash_password(
        data.new_password
    )

    user.reset_token = None

    db.commit()

    return {
        "message": "Password reset successful"
    }