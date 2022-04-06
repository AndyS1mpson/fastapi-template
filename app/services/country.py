from typing import List

from psycopg2 import errors as pg_errors
from pydantic import parse_obj_as
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import app.db.base as models
from app import schemas
from app.exceptions.country import CountryAlreadyExists


def create_country(db: Session, country: schemas.CountryIn) -> schemas.CountryOut:
    db_country = models.Country(**country.dict())
    try:
        models.save(db=db, data=db_country)
    except IntegrityError as e:
        if isinstance(e.orig, pg_errors.UniqueViolation):
            raise CountryAlreadyExists("Country already exists")
        raise

    return schemas.CountryOut(**db_country.__dict__)


def get_all_countries(db: Session) -> List[schemas.CountryOut]:
    all_countries = db.query(models.Country).all()

    return parse_obj_as(List[schemas.CountryOut], all_countries)
