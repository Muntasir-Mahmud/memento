from typing import Any, List

from fastapi import APIRouter, Depends, status
from pydantic import UUID4

from app.core.auth import current_user, superuser
from app.core.pagination import Params

from .models import Topic
from .schemas import TopicRead, TopicCreate, TopicUpdate
from .crud import get_multi, create, update, get, delete

router = APIRouter(tags=['Topics'], prefix='/topics')


@router.get("/", status_code=status.HTTP_200_OK,
            response_model=List[TopicRead],
            dependencies=[Depends(current_user)])
async def read_topics(
        params: Params = Depends()
):
    """
    Get list of topics.
    """
    return await get_multi(params=params)


@router.get("/{topic_id}", status_code=status.HTTP_200_OK,
            response_model=TopicRead,
            dependencies=[Depends(current_user)])
async def read_topic(
        topic_id: UUID4,
) -> Topic:
    """
    Retrieve a topic.
    """
    return await get(topic_id=topic_id)


@router.post("/", status_code=status.HTTP_201_CREATED,
             response_model=TopicCreate,
             dependencies=[Depends(superuser)])
async def create_topic(
        topic_in: TopicCreate
) -> Topic:
    """
    Create new topic.
    """
    return await create(obj_in=topic_in)


@router.put("/{topic_id}", status_code=status.HTTP_200_OK,
            response_model=TopicUpdate,
            dependencies=[Depends(superuser)])
async def update_topic(
        topic_id: UUID4,
        topic_in: TopicUpdate
) -> Topic:
    """
    Update a topic.
    """
    return await update(topic_id=topic_id, obj_in=topic_in)


@router.delete("/{topic_id}", status_code=status.HTTP_204_NO_CONTENT,
               dependencies=[Depends(superuser)])
async def update_topic(
        topic_id: UUID4,
) -> None:
    """
    Update a topic.
    """
    return await delete(topic_id=topic_id)
