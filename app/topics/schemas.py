from pydantic import BaseModel, UUID4
from .models import Topic
from tortoise.contrib.pydantic import pydantic_model_creator


class TopicBase(BaseModel):
    name: str
    description: str


class TopicInDBBase(TopicBase):
    id: UUID4

    class Config:
        from_attributes = True
        primary_key = ("id",)


TopicCreateIn = pydantic_model_creator(Topic, name="TopicCreateIn", exclude=(
    "id", "created_at", "updated_at"), exclude_readonly=True)
TopicUpdateIn = pydantic_model_creator(Topic, name="TopicUpdateIn", exclude=(
    "id", "created_at", "updated_at"))
TopicCreate = pydantic_model_creator(Topic, name="TopicCreate", exclude=(
    "created_at", "updated_at"))
TopicUpdate = pydantic_model_creator(Topic, name="TopicUpdate", exclude=(
    "created_at", "updated_at"))
TopicRead = pydantic_model_creator(Topic, name="TopicRead", exclude=(
    "created_at", "updated_at"))
