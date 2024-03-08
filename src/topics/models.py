import uuid

from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

from src.db import Base


class Topic(Base):
    __tablename__ = "topics"

    topic_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4,
                      unique=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
