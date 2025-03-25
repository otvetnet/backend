import uuid

from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from app.models.session import StudentSession


def create_session(db: Session, student_id: int) -> StudentSession | None:
    try:
        session_token = str(uuid.uuid4())
        expires_at = datetime.now(timezone.utc) + timedelta(hours=2)
        session = StudentSession(session_token=session_token,
                                 user_id=student_id,
                                 expires_at=expires_at)
        db.add(session)
        db.commit()
        db.refresh(session)

        return session
    except Exception as e:
        raise e