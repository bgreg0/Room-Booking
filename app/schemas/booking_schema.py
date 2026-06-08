from uuid import UUID
from datetime import datetime
from pydantic import BaseModel
from app.models.booking import BookingStatus


class BookingBase(BaseModel):
    user_id: UUID
    room_id: UUID
    start_time: datetime
    end_time: datetime


class BookingCreate(BookingBase):
    pass


class BookingRead(BookingBase):
    id: UUID
    status: BookingStatus

    class Config:
        from_attributes = True
