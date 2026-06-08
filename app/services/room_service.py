from sqlalchemy.orm import Session

from app.repositories.room_repo import RoomRepository
from app.models.room import Room


class RoomService:

    @staticmethod
    def create_room(
        session: Session,
        name: str,
        capacity: int,
        floor: int | None,
        building: str | None,
        equipment: dict | None,
    ) -> Room:

        return RoomRepository.create(
            session=session,
            name=name,
            capacity=capacity,
            floor=floor,
            building=building,
            equipment=equipment,
        )

    @staticmethod
    def get_room(session: Session, room_id) -> Room | None:
        return RoomRepository.get_by_id(session, room_id)

    @staticmethod
    def list_rooms(session: Session) -> list[Room]:
        return RoomRepository.list_all(session)
