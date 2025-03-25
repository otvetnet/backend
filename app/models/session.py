from sqlalchemy import Integer, String, Column, ForeignKey, DateTime
from datetime import datetime, timezone
from app.database import Base

class StudentSession(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    user_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    session_token = Column(String, unique=True, index=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    expires_at = Column(DateTime(timezone=True))