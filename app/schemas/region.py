from typing import List

from pydantic import BaseModel

from app.schemas.city import City as CitySchema


class RegionBase(BaseModel):
    name: str


class Region(RegionBase):
    id: int

    class Config:
        from_attributes = True


class RegionWithCities(RegionBase):
    id: int
    cities: List[CitySchema]

    class Config:
        from_attributes = True
