from uuid import UUID

from pydantic import BaseModel


class ApiV1GroupGetSchema(BaseModel):
    id: UUID
    name: str
    number: str


class ApiV1GroupCreateSchema(BaseModel):
    name: str
    number: str
