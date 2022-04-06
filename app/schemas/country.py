from pydantic import Field

from app.schemas import BaseSchema


class CountryOut(BaseSchema):
    id: int
    name: str


class CountryIn(BaseSchema):
    name: str = Field(default="name")
