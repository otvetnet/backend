from sqlalchemy import Integer, Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey("cities.id"))
    school = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    city = relationship("City", back_populates="students")