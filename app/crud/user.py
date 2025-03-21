from sqlalchemy.orm import Session

from app.logger import get_logger
from app.models.user import User
from app.oauth2 import get_password_hash

logger = get_logger()


def create_user(db: Session, first_name: str,
                last_name: str, age: int, password: str) -> User:
    hashed_password = get_password_hash(password)
    user = User(first_name=first_name, last_name=last_name,
                hashed_password=hashed_password, age=age)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
