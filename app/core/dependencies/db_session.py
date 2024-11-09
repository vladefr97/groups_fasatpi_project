from sqlmodel import Session

from app.core.db_config import DB_ENGINE


def session_dependency():
    with Session(DB_ENGINE) as session:
        yield session