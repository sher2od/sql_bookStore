#  SQLAlchemy engine va metadata

from sqlalchemy import create_engine,MetaData
from sqlalchemy import URL
import config

# databazaga ulanihga utl yasaymiz
DATABASE_URL = URL.create(
    "postgresql+psycopg2",
    username=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    port=config.DB_PORT,
    database=config.DB_NAME
)

# engine (Postgresql bilan ulanish)
engine = create_engine(DATABASE_URL)

# Metadata (jadval strukturasi yaratiladi)
metadata_obj = MetaData()
