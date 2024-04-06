from pydantic import BaseModel, UUID4
from .models import Topic
from tortoise.contrib.pydantic import pydantic_model_creator, pydantic_queryset_creator


class TopicBase(BaseModel):
    name: str
    description: str


class TopicInDBBase(TopicBase):
    id: UUID4

    class Config:
        from_attributes = True
        primary_key = ("id",)


TopicCreate = pydantic_model_creator(Topic, name="TopicCreate", exclude=("id", "created_at", "updated_at"), exclude_readonly=True)
TopicUpdate = pydantic_model_creator(Topic, name="TopicUpdate", exclude=("id", "created_at", "updated_at"))
TopicRead = pydantic_model_creator(Topic, name="TopicRead")
