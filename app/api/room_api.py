from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..db import get_session
from app.schemas.room_schema import RoomCreate, RoomRead
from app.services.room_service import RoomService

router = APIRouter(prefix="/rooms", tags=["Rooms"])


@router.post("/", response_model=RoomRead)
def create_room(payload: RoomCreate, session: Session = Depends(get_session)):
    return RoomService.create_room(
        session=session,
        name=payload.name,
        capacity=payload.capacity,
        floor=payload.floor,
        building=payload.building,
        equipment=payload.equipment,
    )


@router.get("/{room_id}", response_model=RoomRead)
def get_room(room_id: str, session: Session = Depends(get_session)):
    room = RoomService.get_room(session, room_id)
    if not room:
        raise ValueError("Room not found")
    return room


@router.get("/", response_model=list[RoomRead])
def list_rooms(session: Session = Depends(get_session)):
    return RoomService.list_rooms(session)
