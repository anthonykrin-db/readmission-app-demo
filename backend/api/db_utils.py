# db_utils.py
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from fastapi import Depends

# PostgreSQL database connection parameters
db_params = {
    'host': 'localhost',
    'port': '5432',
    'database': 'readmission',
    'user': 'postgres',
    'password': 'sE4!salke$5',
    'schema':'demo'
}

def create_connection():
    dbschema = db_params['schema']
    conn = psycopg2.connect(
      dbname=db_params['dbname'],
      user=db_params['user'],
      host=db_params['host'],
      password=db_params['password'],
      port=db_params['port'],
      options=f'-c search_path={dbschema}',
      )
    return conn


def get_db() -> Session:
    """
    Dependency function to get the PostgreSQL database session.

    Returns:
    - SQLAlchemy Session object.
    """

    dbschema = db_params['schema']
    engine = create_engine(
        f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}",
        connect_args={'options': '-csearch_path={}'.format(dbschema)}
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
