from pydantic import BaseModel


class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    age: int
    city_id: int
    school: str


class StudentSchema(BaseModel):
    id: int
    first_name: str
    last_name: str
    city_id: int

    class Config:
        from_attributes = True