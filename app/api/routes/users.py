from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.dependencies import get_user
from app.core.database import get_db
from app.models.user import User
from app.schemas.user import UserScoreResponse, UserExtraInfoRequest, UserResponse, UserScoreReportResponse
from app.services import user_service

router = APIRouter(prefix="/users", tags=["users"])

@router.get(
    "/score",
    response_model=UserScoreResponse,
)
def read_user_score(
        user: User = Depends(get_user)
):
    return user_service.get_user_score(user)

@router.post(
    "/extra",
)
def create_user_extra_info(
        user_request: UserExtraInfoRequest,
        user: User = Depends(get_user),
        db: Session = Depends(get_db)
):
    user_service.create_user_extra_info(user_request, db, user)

@router.get(
    "",
    response_model=UserResponse,
)
def read_user(
        user: User = Depends(get_user)
):
    return user_service.get_user(user)


@router.get(
    "/score/report",
    response_model=UserScoreReportResponse,
)
def get_user_score_report(
    db: Session = Depends(get_db),
    user=Depends(get_user)
):
    return user_service.get_user_score_report(db, user)
