from sqlalchemy.orm import Session

from app import models
from app.db.base_class import Base


def create_country_pg(
    db: Session,
) -> Base:
    country = models.Country(
        name="Russia",
    )
    db.add(country)
    db.commit()

    return country
