from uuid import UUID, uuid4
import enum

from sqlalchemy import DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import TSRANGE
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class BookingStatus(str, enum.Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"


class Booking(Base):
    __tablename__ = "bookings"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid4
    )

    user_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("users.id"), nullable=False
    )
    room_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey("rooms.id"), nullable=False
    )

    start_time: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)
    end_time: Mapped[DateTime] = mapped_column(DateTime(timezone=True), nullable=False)

    time_range: Mapped[tuple] = mapped_column(TSRANGE, nullable=False)

    status: Mapped[BookingStatus] = mapped_column(
        Enum(BookingStatus, name="booking_status"),
        default=BookingStatus.CONFIRMED,
        nullable=False,
    )

    user: Mapped["User"] = relationship(back_populates="bookings")
    room: Mapped["Room"] = relationship(back_populates="bookings")
