from fastapi import APIRouter, Depends, Response
from sqlmodel import Session

from api.db import get_user, get_session

router = APIRouter(tags=["users"], prefix="/users")


@router.get("/{id}")
async def get_user_by_id(*, session: Session = Depends(get_session), id: int):
    user = get_user(session, id)
    if user is None:
        return Response(status_code=404)
    return user
