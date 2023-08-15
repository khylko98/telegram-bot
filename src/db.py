import config

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from contextlib import contextmanager


if not config.DATABASE_URL:
    raise ValueError(
        "DATABASE_URL env variable wasn't implemented in .env "
        "(should be initialized)."
    )

engine = create_engine(config.DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_context = contextmanager(get_db)
