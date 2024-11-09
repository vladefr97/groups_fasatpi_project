from sqlmodel import Session, select

from app.db.models import GroupModel
from app.domain.entities import Group
from app.persistance.base import BaseGroupPersistence


class PostgresGroupPersistence(BaseGroupPersistence):
    def __init__(self, session: Session):
        self.__session = session

    def get_by_id(self, group_id: int) -> Group | None:
        query = select(GroupModel).where(GroupModel.id == group_id)
        group = self.__session.exec(query).first()
        return Group(id=group.id, name=group.name, number=group.group_number)

    def create_group(self, group: Group) -> None:
        db_group = GroupModel(name=group.name, group_number=group.number, chief="")
        self.__session.add(db_group)
        self.__session.commit()
        self.__session.refresh(db_group)

