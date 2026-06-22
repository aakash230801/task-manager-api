from fastapi import APIRouter
from fastapi import Depends

from app.schemas.user_schema import UserCreate
from app.facades.user_facade import UserFacade

from app.core.database import get_db

router = APIRouter()

@router.post("/users")
def create_user(
    payload: UserCreate,
    db=Depends(get_db)
):

    facade = UserFacade(db)

    return facade.create_user(payload)