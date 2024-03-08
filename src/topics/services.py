from typing import List

from . import models


async def get_all_topics(database) -> List[models.Topic]:
    topics = database.query(models.Topic).all()
    return topics
