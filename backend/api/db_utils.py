# db_utils.py
import psycopg2
import hashlib
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from fastapi import Depends

# PostgreSQL database connection parameters
db_params = {
    'host': 'localhost',
    'port': '5432',
    'database': 'readmission',
    'user': 'postgres',
    'password': 'sE4!salke$5'
}

def create_connection():
    return psycopg2.connect(**db_params)


def get_database_session() -> Session:
    """
    Dependency function to get the PostgreSQL database session.

    Returns:
    - SQLAlchemy Session object.
    """
    engine = create_engine(
        f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}"
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
