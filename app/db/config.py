from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.core.config import settings

# TODO: take the credentials from settings
TORTOISE_ORM = {
    "connections": {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': 'localhost',
                'port': '5432',
                'user': 'muntasir',
                'password': 'Siyam529',
                'database': 'memento',
            }
        }
    },
    "apps": {
        "models": {
            "models": [
                "aerich.models",
                "app.users.models",
                "app.topics.models",
                "app.cards.models",
            ],
            "default_connection": "default",
        },
    },
}


def register_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,
        add_exception_handlers=True,
    )
