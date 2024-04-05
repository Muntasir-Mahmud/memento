from fastapi.encoders import jsonable_encoder

from app.core.pagination import Page, Params, paginate

from .models import Topic
from .schemas import TopicCreate, TopicRead


async def get_multi(
         params: Params
) -> Page[TopicRead]:
    return await paginate(Topic.all(), params, TopicRead)


async def create(
        obj_in: TopicCreate
) -> Topic:
    obj_in_data = jsonable_encoder(obj_in)
    return await Topic.create(**obj_in_data)
