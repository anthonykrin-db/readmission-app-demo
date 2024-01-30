# db_utils.py
import psycopg2
import hashlib

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

def md5_hash(password):
    return hashlib.md5(password.encode()).hexdigest()
