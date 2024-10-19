from pydantic import BaseModel


class Group(BaseModel):
    id: int
    name: str
    number: str
