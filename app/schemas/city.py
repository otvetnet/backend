from pydantic import BaseModel


class CityBase(BaseModel):
    name: str
    region_id: int


class City(CityBase):
    id: int

    class Config:
        from_attributes = True