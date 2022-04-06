from sqlalchemy import Column, Integer, String

from app.db.base_class import Base


class Country(Base):
    __tablename__ = "country"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    def __repr__(self) -> str:
        return f"{self.id} {self.name}"
