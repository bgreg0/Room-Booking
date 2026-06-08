from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.user import User


class UserRepository:

    @staticmethod
    def create(session: Session, first_name: str, last_name: str, email: str) -> User:
        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    @staticmethod
    def get_by_id(session: Session, user_id):
        return session.get(User, user_id)

    @staticmethod
    def get_by_email(session: Session, email: str):
        stmt = select(User).where(User.email == email)
        return session.scalar(stmt)

    @staticmethod
    def list_all(session: Session):
        stmt = select(User)
        return session.scalars(stmt).all()
