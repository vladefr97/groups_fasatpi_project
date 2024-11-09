from pydantic import PostgresDsn
from sqlmodel import create_engine

from app.core.config import SETTINGS

print(SETTINGS)
#
# DB_URI = PostgresDsn.build(
#     scheme='postgresql',
#     user=SETTINGS.DB_USER,
#     password=SETTINGS.DB_PASSWORD,
#     host=f"{SETTINGS.DB_HOSTNAME}:{SETTINGS.DB_PORT}",
#     path=f"/{SETTINGS.DB_NAME}"
# )

DB_URI = f"postgresql://{SETTINGS.DB_USER}:{SETTINGS.DB_PASSWORD}@{SETTINGS.DB_HOSTNAME}:{SETTINGS.DB_PORT}/{SETTINGS.DB_NAME}"

DB_ENGINE = create_engine(DB_URI)