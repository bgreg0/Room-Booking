from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.user_api import router as users_router
from app.api.room_api import router as rooms_router
from app.api.booking_api import router as bookings_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Meeting Room Booking System",
        version="1.0.0",
    )

    # CORS (adjust origins for production)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routers
    app.include_router(users_router)
    app.include_router(rooms_router)
    app.include_router(bookings_router)

    return app
