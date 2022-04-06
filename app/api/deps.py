from typing import Generator, Optional

from sqlalchemy.orm import Session

from app.db.session import SessionLocalPG


def get_db_pg() -> Generator:
    db: Optional[Session] = None
    try:
        db = SessionLocalPG()
        yield db
    finally:
        if db is not None:
            db.close()
