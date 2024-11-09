from uuid import UUID, uuid4

from sqlmodel import SQLModel, Field


class GroupModel(SQLModel, table=True):
    __tablename__ = "group"

    id: UUID = Field(
        primary_key=True,
        default_factory=uuid4
    )

    name: str = Field(
        max_length=100,
        unique=True
    )

    group_number: str = Field(
        max_length=100,
        unique=True
    )

    chief: str = Field(
        max_length=100
    )

