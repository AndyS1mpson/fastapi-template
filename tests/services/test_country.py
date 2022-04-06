import pytest
from sqlalchemy.orm import Session

from app import schemas, services
from tests.utils import COUNTRY_NAME

pytestmark = pytest.mark.usefixtures("use_postgres")


def test_create_county(pg_session: Session) -> None:
    country_in = {"name": COUNTRY_NAME}

    country = services.create_country(
        db=pg_session,
        country=schemas.CountryIn(**country_in),
    )

    assert isinstance(country, schemas.CountryOut)

    assert isinstance(country.id, int)

    assert isinstance(country.name, str)
    assert country.name == COUNTRY_NAME
