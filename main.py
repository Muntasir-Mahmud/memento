from fastapi import FastAPI

from src.topics import router as topic_router


description = """
Memento API
"""

app = FastAPI(
    title="Memento",
    description=description,
    version="0.0.1",
    contact={
        "name": "Muntasir Mahmud",
        "url": "http://x-force.example.com/contact/",
    },

)

app.include_router(topic_router.router)
