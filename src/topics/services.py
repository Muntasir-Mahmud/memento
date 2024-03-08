from typing import List

from . import models


async def get_all_categories(database) -> List[models.Topic]:
    topics = database.query(models.Topic).all()
    return topics
