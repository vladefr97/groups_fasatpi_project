from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class Group(BaseModel):
    id: Optional[UUID]
    name: str
    number: str
