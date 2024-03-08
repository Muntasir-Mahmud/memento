from typing import List, Type

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from .models import Topic as TopicModel
from .schema import TopicCreate, Topic


def get_multi(
        db: Session, *, skip: int = 0, limit: int = 100
) -> List[Type[Topic]]:
    return db.query(TopicModel).offset(skip).limit(limit).all()


def create(
        db: Session,
        *,
        obj_in: TopicCreate
) -> TopicModel:
    obj_in_data = jsonable_encoder(obj_in)
    db_obj = TopicModel(**obj_in_data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
