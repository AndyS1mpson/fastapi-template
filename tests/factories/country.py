import factory
from pytest_factoryboy import register

from app import models
from tests.common import PGSession


@register
class CountryFactory(factory.alchemy.SQLAlchemyModelFactory):
    name = factory.Sequence(lambda n: f"country {n}")

    class Meta:
        model = models.Country
        sqlalchemy_session = PGSession
        sqlalchemy_session_persistence = "flush"
