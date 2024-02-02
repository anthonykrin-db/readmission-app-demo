#misc_utils.py

import hashlib
import uuid

def md5_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

def generate_guid():
    """
    Generate and return a GUID (UUID4).
    """
    return str(uuid.uuid4())
