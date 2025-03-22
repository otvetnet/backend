from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.city import fetch_cities
from app.crud.region import fetch_regions, fetch_region_with_cities
from app.database import get_db
from app.logger import get_logger

from app.schemas.region import Region as RegionSchema
from app.schemas.region import RegionWithCities
from app.schemas.city import City as CitySchema

logger = get_logger()
router = APIRouter()


@router.get("/regions", response_model=List[RegionSchema])
def get_regions(db: Session = Depends(get_db)):
    return fetch_regions(db)


@router.get("/cities", response_model=List[CitySchema])
def get_cities(db: Session = Depends(get_db)):
    return fetch_cities(db)


@router.get("/cities/by-region/{region_id}", response_model=RegionWithCities)
def get_cities_by_region_id(region_id: int, db: Session = Depends(get_db)):
    return fetch_region_with_cities(db, region_id)
