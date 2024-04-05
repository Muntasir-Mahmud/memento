from pydantic import BaseModel, UUID4


class TopicBase(BaseModel):
    name: str
    description: str


class TopicInDBBase(TopicBase):
    id: UUID4

    class Config:
        from_attributes = True
        primary_key = ("id",)


class TopicCreate(TopicBase):
    pass


class TopicUpdate(TopicBase):
    pass


class TopicRead(TopicInDBBase):
    pass
