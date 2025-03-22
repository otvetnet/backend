from sqlalchemy.orm import Session

from app.logger import get_logger
from app.models.city import City

logger = get_logger()


def fetch_cities(db: Session):
    return db.query(City).all()
