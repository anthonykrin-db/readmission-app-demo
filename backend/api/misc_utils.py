#misc_utils.py

import hashlib
import uuid

def md5_hash(clr_txt):
    return hashlib.md5(clr_txt.encode()).hexdigest()

def generate_guid():
    """
    Generate and return a GUID (UUID4).
    """
    return str(uuid.uuid4())
