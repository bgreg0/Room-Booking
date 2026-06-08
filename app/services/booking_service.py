from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.repositories.booking_repo import BookingRepository
from app.repositories.user_repo import UserRepository
from app.repositories.room_repo import RoomRepository
from app.models.booking import Booking, BookingStatus


class BookingService:

    @staticmethod
    def create_booking(
        session: Session,
        user_id,
        room_id,
        start_time: datetime,
        end_time: datetime,
    ) -> Booking:

        if start_time >= end_time:
            raise ValueError("Start time must be before end time.")

        if not UserRepository.get_by_id(session, user_id):
            raise ValueError("User does not exist.")

        if not RoomRepository.get_by_id(session, room_id):
            raise ValueError("Room does not exist.")

        time_range = func.tsrange(start_time, end_time, "[]")

        return BookingRepository.create(
            session=session,
            user_id=user_id,
            room_id=room_id,
            start_time=start_time,
            end_time=end_time,
            time_range=time_range,
            status=BookingStatus.CONFIRMED,
        )

    @staticmethod
    def get_booking(session: Session, booking_id) -> Booking | None:
        return BookingRepository.get_by_id(session, booking_id)

    @staticmethod
    def list_bookings(session: Session) -> list[Booking]:
        return BookingRepository.list_all(session)

    @staticmethod
    def list_bookings_for_room(session: Session, room_id) -> list[Booking]:
        return BookingRepository.list_for_room(session, room_id)

    @staticmethod
    def list_bookings_for_user(session: Session, user_id) -> list[Booking]:
        return BookingRepository.list_for_user(session, user_id)

    @staticmethod
    def cancel_booking(session: Session, booking_id) -> Booking | None:
        return BookingRepository.cancel(session, booking_id)
