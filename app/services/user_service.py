from sqlalchemy.orm import Session

from app.repositories.user_repo import UserRepository
from app.models.user import User


class UserService:

    @staticmethod
    def create_user(
        session: Session,
        first_name: str,
        last_name: str,
        email: str,
    ) -> User:

        existing = UserRepository.get_by_email(session, email)
        if existing:
            raise ValueError("A user with this email already exists.")

        return UserRepository.create(
            session=session,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )

    @staticmethod
    def get_user(session: Session, user_id) -> User | None:
        return UserRepository.get_by_id(session, user_id)

    @staticmethod
    def list_users(session: Session) -> list[User]:
        return UserRepository.list_all(session)
