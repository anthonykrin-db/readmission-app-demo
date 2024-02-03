#misc_utils.py

import hashlib
import uuid
from datetime import datetime

def md5_hash(clr_txt):
    return hashlib.md5(clr_txt.encode()).hexdigest()

def generate_guid():
    """
    Generate and return a GUID (UUID4).
    """
    return str(uuid.uuid4())


def is_valid_date(date_str):
    try:
        # Try to convert the string to a date.
        # You might want to specify a format, if your date strings are not ISO format
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def convert_date(date_str:str,  default_date:datetime=datetime.now()):
    if is_valid_date(date_str):
        return datetime.strptime(date_str, '%Y-%m-%d')
    else:
        return default_date

