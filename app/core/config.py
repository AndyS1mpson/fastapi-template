import logging
from pathlib import Path
from typing import Any, Mapping, Optional

from pydantic import BaseSettings, HttpUrl, PostgresDsn, validator


class Settings(BaseSettings):
    SENTRY_DSN: Optional[HttpUrl] = None

    BASE_DIR: Path = Path(__file__).absolute().parent.parent
    STATIC_DIR: Path = BASE_DIR / "statics"

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str = ""
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str
    POSTGRES_TEST_DB: str = ""

    POSTGRES_URL: str = ""
    TEST_POSTGRES_URL: str = ""

    @validator("POSTGRES_URL", pre=True)
    def assemble_postgres_db_url(
        cls, v: Optional[str], values: Mapping[str, Any]
    ) -> Any:
        if v and isinstance(v, str):
            return v

        return str(
            PostgresDsn.build(
                scheme="postgresql",
                user=values["POSTGRES_USER"],
                password=values["POSTGRES_PASSWORD"],
                host=values["POSTGRES_HOST"],
                port=str(values["POSTGRES_PORT"]),
                path=f'/{values["POSTGRES_DB"]}',
            )
        )

    @validator("TEST_POSTGRES_URL", pre=True)
    def assemble_test_postgres_url(
        cls, v: Optional[str], values: Mapping[str, Any]
    ) -> Any:
        if not values.get("POSTGRES_TEST_DB"):
            return ""
        if v and isinstance(v, str):
            return v

        return str(
            PostgresDsn.build(
                scheme="postgresql",
                user=values["POSTGRES_USER"],
                password=values["POSTGRES_PASSWORD"],
                host=values["POSTGRES_HOST"],
                port=str(values["POSTGRES_PORT"]),
                path=f'/{values["POSTGRES_TEST_DB"]}',
            )
        )


settings = Settings()

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)
