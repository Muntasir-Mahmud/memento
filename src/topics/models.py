import uuid

from sqlalchemy import Column, Integer, String, relationship, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from src.db import Base


class Topic(Base):
    __tablename__ = "topics"

    topic_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    parent_topic_id = Column(Integer, ForeignKey("topics.topic_id"))

    children = relationship("Topic", cascade="all, delete-orphan", backref="parent")
    cards = relationship("Card", backref="topic")
