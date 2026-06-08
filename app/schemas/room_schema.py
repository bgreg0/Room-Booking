from uuid import UUID
from pydantic import BaseModel


class RoomBase(BaseModel):
    name: str
    capacity: int
    floor: int | None = None
    building: str | None = None
    equipment: dict | None = None


class RoomCreate(RoomBase):
    pass


class RoomRead(RoomBase):
    id: UUID

    class Config:
        from_attributes = True
