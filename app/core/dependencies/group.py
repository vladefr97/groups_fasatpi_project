from app.persistance.base import BaseGroupPersistence
from app.persistance.dictionary import GroupDictionaryPersistence


def group_persistence_dependency() -> BaseGroupPersistence:
    return GroupDictionaryPersistence()
