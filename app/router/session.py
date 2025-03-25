from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.crud.session import create_session
from app.crud.student import create_student

from app.database import get_db
from app.logger import get_logger
from app.schemas.session import SessionResponse
from app.schemas.student import StudentCreate

router = APIRouter()
logger = get_logger()


@router.post("/create", response_model=SessionResponse)
def session_create(student: StudentCreate, db: Session = Depends(get_db)):
    try:
        new_student = create_student(student, db)
        new_session = create_session(db, new_student.id)

        return SessionResponse(
            session_token=new_session.session_token,
            expires_at=new_session.expires_at
        )
    except Exception as e:
        raise e