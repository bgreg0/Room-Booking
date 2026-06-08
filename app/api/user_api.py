from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import get_session
from app.schemas.user_schema import UserCreate, UserRead
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserRead)
def create_user(payload: UserCreate, session: Session = Depends(get_session)):
    return UserService.create_user(
        session=session,
        first_name=payload.first_name,
        last_name=payload.last_name,
        email=payload.email,
    )


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: str, session: Session = Depends(get_session)):
    user = UserService.get_user(session, user_id)
    if not user:
        raise ValueError("User not found")
    return user


@router.get("/", response_model=list[UserRead])
def list_users(session: Session = Depends(get_session)):
    return UserService.list_users(session)
