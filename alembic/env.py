import os
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv
from core.database import Base

# Load environment variables first
load_dotenv()


# Alembic Config object
config = context.config

# Read DATABASE_URL from .env
database_url = os.getenv("DATABASE_URL")

if database_url:
    config.set_main_option(
        "sqlalchemy.url",
        database_url
    )

# Configure logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


# Metadata for autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """
    Run migrations in offline mode.

    Alembic uses the configured database URL to generate migration
    SQL without creating an engine or opening a database connection.

    Useful for generating migration scripts and reviewing schema
    changes before execution.
    """

    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """
    Run migrations using an active database connection.

    Alembic creates a SQLAlchemy engine, connects to the target
    database, and applies pending migrations directly against
    the configured schema.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
