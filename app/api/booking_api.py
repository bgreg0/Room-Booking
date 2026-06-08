from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import get_session
from app.schemas.booking_schema import BookingCreate, BookingRead
from app.services.booking_service import BookingService

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.post("/", response_model=BookingRead)
def create_booking(payload: BookingCreate, session: Session = Depends(get_session)):
    return BookingService.create_booking(
        session=session,
        user_id=payload.user_id,
        room_id=payload.room_id,
        start_time=payload.start_time,
        end_time=payload.end_time,
    )

@router.get("/", response_model=list[BookingRead])
def list_bookings(session: Session = Depends(get_session)):
    return BookingService.list_bookings(session)

@router.get("/{booking_id}", response_model=BookingRead)
def get_booking(booking_id: str, session: Session = Depends(get_session)):
    booking = BookingService.get_booking(session, booking_id)
    if not booking:
        raise ValueError("Booking not found")
    return booking


@router.get("/room/{room_id}", response_model=list[BookingRead])
def list_bookings_for_room(room_id: str, session: Session = Depends(get_session)):
    return BookingService.list_bookings_for_room(session, room_id)


@router.get("/user/{user_id}", response_model=list[BookingRead])
def list_bookings_for_user(user_id: str, session: Session = Depends(get_session)):
    return BookingService.list_bookings_for_user(session, user_id)


@router.delete("/{booking_id}", response_model=BookingRead)
def cancel_booking(booking_id: str, session: Session = Depends(get_session)):
    booking = BookingService.cancel_booking(session, booking_id)
    if not booking:
        raise ValueError("Booking not found")
    return booking
