import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Get the database URL from an environment variable
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")


#Configure the engine with the appropriate parameters for PostgreSQL
engine = create_engine(
    SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()