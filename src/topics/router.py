from typing import List, Any

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from src.db import get_db

from . import schema
from . import crud

router = APIRouter(tags=['Topics'], prefix='/topics')


@router.get('/', status_code=status.HTTP_200_OK,
            response_model=List[schema.Topic])
def read_topics(
        db: Session = Depends(get_db),
        skip: int = 0,
        limit: int = 100
) -> Any:
    """
    Retrieve topics.
    """
    return crud.get_multi(db, skip=skip, limit=limit)


@router.post("/create", status_code=status.HTTP_201_CREATED,
             response_model=schema.Topic)
def create_restaurant(
        *,
        db: Session = Depends(get_db),
        topic_in: schema.TopicCreate
) -> Any:
    """
    Create new topic.
    """
    restaurant = crud.create(db=db, obj_in=topic_in)
    return restaurant
