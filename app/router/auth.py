from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.user import create_user
from app.database import get_db
from app.logger import get_logger
from app.schemas.user import UserCreate, User

router = APIRouter()
logger = get_logger()


@router.post("/signup", response_model=User)
async def signup(user: UserCreate, db: Session = Depends(get_db)):
    try:
        new_user = create_user(db=db,
                               first_name=user.first_name,
                               last_name=user.last_name,
                               password=user.password,
                               age=user.age)
        logger.info(f"created new user:{new_user.id}")
        return new_user
    except ValueError as e:
        logger.error(f"error creating user ${e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=e)
