from __future__ import with_statement

import os
import sys
from logging.config import fileConfig

from sqlalchemy.engine import Engine
from sqlalchemy.schema import MetaData

from alembic import context
from app.db.base import Base
from app.db.session import postgres_engine

parent_dir = os.path.abspath(os.getcwd())
sys.path.append(parent_dir)

config = context.config
fileConfig(config.config_file_name)


class Migrator:
    def __init__(self, engine: Engine, target_metadata: MetaData) -> None:
        self.engine = engine
        self.target_metadata = target_metadata

    def migrate(self) -> None:
        connectable = config.attributes.get("connection", None)
        if connectable is None:
            connectable = self.engine.connect()
        context.configure(
            connection=connectable,
            target_metadata=self.target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            self.prepare_migration_context()
            context.run_migrations()

    def prepare_migration_context(self) -> None:
        pass


class PostgresMigrator(Migrator):
    pass


def run_migrations_online() -> None:
    if config.config_ini_section == "postgres":
        migrator = PostgresMigrator(postgres_engine, Base.metadata)

    migrator.migrate()


run_migrations_online()
