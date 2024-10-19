from pydantic import BaseModel


class ApiV1GroupGetSchema(BaseModel):
    id: int
    name: str
    number: str


class ApiV1GroupCreateSchema(BaseModel):
    id: int
    name: str
    number: str
