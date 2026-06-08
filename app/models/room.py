from uuid import UUID, uuid4
from sqlalchemy import String, Integer
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class Room(Base):
    __tablename__ = "rooms"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid4
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    capacity: Mapped[int] = mapped_column(Integer, nullable=False)
    floor: Mapped[int | None] = mapped_column(Integer, nullable=True)
    building: Mapped[str | None] = mapped_column(String, nullable=True)
    equipment: Mapped[dict | None] = mapped_column(JSONB, nullable=True)

    bookings: Mapped[list["Booking"]] = relationship(
        back_populates="room", cascade="all, delete-orphan"
    )
