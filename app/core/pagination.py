from __future__ import annotations

from typing import Generic, TypeVar, List, Type

from pydantic import BaseModel, Field
from tortoise.queryset import QuerySet

from .config import settings

T = TypeVar("T", bound=BaseModel)


class Params(BaseModel):
    limit: int = Field(settings.PAGINATION_PER_PAGE, gt=0)
    offset: int = Field(0, gt=-1)


class Page(BaseModel, Generic[T]):
    items: List[T]
    total: int


# TODO: rewrite the pagination
async def paginate(items: QuerySet, params: Params, pydantic_model: Type[BaseModel]) -> Page:
    offset = params.offset
    limit = params.limit

    fetched_items = await items.limit(limit).offset(offset).order_by("-created_at")
    model_instances = [pydantic_model(**dict(item)) for item in fetched_items]

    return Page(items=model_instances, total=await items.count())
