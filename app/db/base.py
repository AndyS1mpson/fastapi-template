# flake8: noqa
from sqlalchemy.orm import Session

from app.db.base_class import Base
from app.models import *


def save(db: Session, data: Base) -> None:
    db.add(data)
    db.commit()
    db.refresh(data)
