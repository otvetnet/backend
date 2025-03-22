from sqlalchemy import or_
from sqlalchemy.orm import Session, joinedload

from app.logger import get_logger
from app.models.region import Region

logger = get_logger()


def fetch_regions(db: Session):
    return db.query(Region).all()

def fetch_region_with_cities(db: Session, region_id: int):
    return (
        db.query(Region)
        .options(joinedload(Region.cities))
        .filter(or_(Region.id == region_id))
        .first()
    )