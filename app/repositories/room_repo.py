from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.room import Room


class RoomRepository:

    @staticmethod
    def create(
        session: Session,
        name: str,
        capacity: int,
        floor: int | None,
        building: str | None,
        equipment: dict | None,
    ) -> Room:
        room = Room(
            name=name,
            capacity=capacity,
            floor=floor,
            building=building,
            equipment=equipment,
        )
        session.add(room)
        session.commit()
        session.refresh(room)
        return room

    @staticmethod
    def get_by_id(session: Session, room_id):
        return session.get(Room, room_id)

    @staticmethod
    def get_by_code(session: Session, code: str):
        stmt = select(Room).where(Room.code == code)
        return session.scalar(stmt)

    @staticmethod
    def list_all(session: Session):
        stmt = select(Room)
        return session.scalars(stmt).all()
