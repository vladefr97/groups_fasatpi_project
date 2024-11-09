from logging.config import fileConfig

from alembic.script import ScriptDirectory

from alembic import context
from sqlmodel import SQLModel

from app.core.db_config import DB_ENGINE, DB_URI
from app.db.models import *

config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = SQLModel.metadata


def process_revision_directives(context, revision, directives) -> None:  # type: ignore
    if config.cmd_opts and config.cmd_opts.autogenerate:
        script = directives[0]

        if script.upgrade_ops.is_empty():
            directives[:] = []
            print("No changes detected.")
        else:
            head_revision = ScriptDirectory.from_config(config).get_current_head()

            if head_revision is None:
                new_rev_id = 1
            else:
                last_rev_id = int(head_revision.lstrip("0"))
                new_rev_id = last_rev_id + 1
            script.rev_id = "{0:04}".format(new_rev_id)


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

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
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    with DB_ENGINE.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            process_revision_directives=process_revision_directives,
            compare_type=True,
            dialect_opts={"paramstyle": "named"},
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
