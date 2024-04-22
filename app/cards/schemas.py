from tortoise.contrib.pydantic import pydantic_model_creator
from .models import Card


CardCreateIn = pydantic_model_creator(Card, name="CardCreateIn", exclude=(
    "id", "created_at", "updated_at"), exclude_readonly=True)
CardUpdateIn = pydantic_model_creator(Card, name="CardUpdateIn", exclude=(
    "id", "created_at", "updated_at"))
CardCreate = pydantic_model_creator(Card, name="CardCreate", exclude=(
    "created_at", "updated_at"))
CardUpdate = pydantic_model_creator(Card, name="CardUpdate", exclude=(
    "created_at", "updated_at"))
CardRead = pydantic_model_creator(Card, name="CardRead", exclude=(
    "created_at", "updated_at"))
