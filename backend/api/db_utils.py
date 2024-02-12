# db_utils.py
from pydoc import text

import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# PostgreSQL database connection parameters
db_params = {
  'host': 'localhost',
  'port': '5432',
  'database': 'readmission',
  'user': 'postgres',
  'password': 'sE4!salke$5',
  'schema': 'demo'
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


def get_schema():
  return db_params['schema']


def get_engine():
  dbschema = db_params['schema']
  connection_url = f"postgresql://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}"
  print("connection_url:" + connection_url)
  engine = create_engine(connection_url, connect_args={'options': '-c search_path={}'.format(dbschema)})
  return engine


def get_session():
  dbschema = db_params['schema']
  sess = Session(get_engine())
  sql_expression = text('SET search_path TO demo')
  sess.execute(sql_expression)
  try:
    yield sess
  finally:
    sess.close()
