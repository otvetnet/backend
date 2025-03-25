from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class City(Base):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    region_id = Column(Integer, ForeignKey("regions.id"))

    region = relationship("Region", back_populates="cities")
    students = relationship("Student", back_populates="city")