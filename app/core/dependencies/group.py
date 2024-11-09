from fastapi import Depends
from sqlmodel import Session

from app.core.dependencies.db_session import session_dependency
from app.persistance.base import BaseGroupPersistence
from app.persistance.postgres import PostgresGroupPersistence


def group_persistence_dependency(session: Session = Depends(session_dependency)) -> BaseGroupPersistence:
    return PostgresGroupPersistence(session)
