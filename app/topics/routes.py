from typing import Any

from fastapi import APIRouter, Depends, status

from app.core.auth import current_user, superuser
from app.core.pagination import Page, Params, paginate

from .models import Topic
from .schemas import TopicRead, TopicCreate, TopicUpdate
from .crud import get_multi, create

router = APIRouter(tags=['Topics'], prefix='/topics')


@router.get("/", status_code=status.HTTP_200_OK,
            response_model=Page[TopicRead],
            dependencies=[Depends(current_user)])
async def read_topics(
        params: Params = Depends()
) -> Page[TopicRead]:
    """
    Get list of topics.
    """
    return await get_multi(params)


@router.post("/create", status_code=status.HTTP_201_CREATED,
             response_model=TopicCreate,
             dependencies=[Depends(superuser)])
async def create_topic(
        topic_in: TopicCreate
) -> Topic:
    """
    Create new topic.
    """
    return await create(obj_in=topic_in)
