from fastapi import APIRouter, Depends, status

from app.core.auth import current_user, fastapi_users
from app.core.pagination import Page, Params, paginate

from .models import User
from .schemas import UserRead, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/",
            status_code=status.HTTP_200_OK,
            response_model=Page[UserRead],
            dependencies=[Depends(current_user)])
async def user_list(params: Params = Depends()):
    return await paginate(User.all(), params)


router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate))
