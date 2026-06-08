from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from sqlalchemy import select, and_
from psycopg2.errors import ExclusionViolation

from app.models.booking import Booking, BookingStatus


class BookingRepository:

    @staticmethod
    def create(
        session: Session,
        user_id,
        room_id,
        start_time,
        end_time,
        time_range,
        status: BookingStatus = BookingStatus.CONFIRMED,
    ) -> Booking:
        booking = Booking(
            user_id=user_id,
            room_id=room_id,
            start_time=start_time,
            end_time=end_time,
            time_range=time_range,
            status=status,
        )

        session.add(booking)

        try:
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            if hasattr(e, "orig") and isinstance(e.orig, ExclusionViolation):
                raise ValueError("This room is already booked for that time range.") from e
            raise

        session.refresh(booking)
        return booking

    @staticmethod
    def get_by_id(session: Session, booking_id):
        return session.get(Booking, booking_id)

    @staticmethod
    def list_for_room(session: Session, room_id):
        stmt = select(Booking).where(Booking.room_id == room_id)
        return session.scalars(stmt).all()

    @staticmethod
    def list_for_user(session: Session, user_id):
        stmt = select(Booking).where(Booking.user_id == user_id)
        return session.scalars(stmt).all()

    @staticmethod
    def list_all(session: Session):
        stmt = select(Booking)
        return session.scalars(stmt).all()

    @staticmethod
    def cancel(session: Session, booking_id):
        booking = session.get(Booking, booking_id)
        if not booking:
            return None

        booking.status = BookingStatus.CANCELLED
        session.commit()
        session.refresh(booking)
        return booking
