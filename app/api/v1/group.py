from fastapi import APIRouter, Depends

from app.api.v1.schemas.group import ApiV1GroupGetSchema, ApiV1GroupCreateSchema
from app.core.dependencies.group import group_persistence_dependency
from app.domain.entities import Group
from app.persistance.base import BaseGroupPersistence

router = APIRouter()


@router.get("/", summary="Information about single group", response_model=ApiV1GroupGetSchema | None)
async def get_group(group_id: int,
                    group_persistence: BaseGroupPersistence = Depends(group_persistence_dependency)) -> ApiV1GroupGetSchema | None:
    group = group_persistence.get_by_id(group_id)
    if group:
        return ApiV1GroupGetSchema(id=group.id, name=group.name, number=group.number)
    else: return None


@router.post("/", summary="Create new group", response_model= None)
async def create_group(group_to_create: ApiV1GroupCreateSchema,
                       group_persistence: BaseGroupPersistence = Depends(group_persistence_dependency)) -> None:
    group = Group(id=group_to_create.id,name=group_to_create.name, number=group_to_create.number)
    group_persistence.create_group(group)

