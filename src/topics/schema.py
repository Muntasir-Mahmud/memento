import uuid
from typing import Optional

from pydantic import BaseModel, Field, UUID4


class TopicBase(BaseModel):
    topic_id: UUID4 = Field(default_factory=uuid.uuid4)
    name: str
    description: str
    parent_topic_id: Optional[UUID4] = None


class TopicList(TopicBase):
    class Config:
        from_attributes = True
        primary_key = ("topic_id",)
