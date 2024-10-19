from abc import ABC

from app.domain.entities import Group


class BaseGroupPersistence(ABC):
    def get_by_id(self, group_id: int) -> Group:
        ...

    def create_group(self, group: Group) -> None:
        ...