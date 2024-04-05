from typing import Union, Dict, Any

from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import UUID4

from app.core.pagination import Page, Params, paginate

from .models import Topic
from .schemas import TopicCreate, TopicRead, TopicUpdate


async def get_multi(
         params: Params
) -> Page[TopicRead]:
    return await paginate(Topic.all(), params, TopicRead)


async def get(
        topic_id: UUID4
) -> Topic:
    return await Topic.get(id=topic_id)


async def create(
        obj_in: TopicCreate
) -> Topic:
    obj_in_data = jsonable_encoder(obj_in)
    return await Topic.create(**obj_in_data)


async def update(
        topic_id: UUID4,
        obj_in: Union[TopicUpdate, Dict[str, Any]]
) -> Topic:
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.dict(exclude_unset=True)
    await Topic.filter(id=topic_id).update(**update_data)
    return await Topic.get(id=topic_id)


async def delete(
        topic_id: UUID4
) -> bool:
    deleted_obj = await Topic.filter(id=topic_id).delete()
    if not deleted_obj:
        raise HTTPException(
            status_code=404,
            detail=f"User {topic_id} not found"
        )
    return True
