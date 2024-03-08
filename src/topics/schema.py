import uuid
from typing import Optional

from pydantic import BaseModel, Field, UUID4


class TopicBase(BaseModel):
    name: str
    description: str
    # parent_topic_id: Optional[UUID4] = None


class TopicInDBBase(TopicBase):
    topic_id: UUID4

    class Config:
        from_attributes = True
        primary_key = ("topic_id",)


class TopicCreate(TopicBase):
    pass


class TopicUpdate(TopicBase):
    pass


class Topic(TopicInDBBase):
    pass


