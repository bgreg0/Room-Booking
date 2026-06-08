from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Session
from contextlib import contextmanager
from dotenv import load_dotenv
import os

load_dotenv()

class Base(DeclarativeBase):
    pass

engine = create_engine(os.getenv("DB_URL"))

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    class_=Session,
)

def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
