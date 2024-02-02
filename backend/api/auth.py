from fastapi import APIRouter
from api.db_utils import create_connection
from api.misc_utils import md5_hash
from pydantic import BaseModel
from fastapi.responses import JSONResponse

router = APIRouter()

# Class for credential
class Credential(BaseModel):
    username: str
    password: str

@router.post('/login')
async def login(credential:Credential):

    if not credential.username or not credential.password:
        return JSONResponse(content={'error': 'Username and password are required'}, status_code=400)

    try:
        conn = create_connection()
        cursor = conn.cursor()

        # Check if the user exists in the database
        cursor.execute("SELECT * FROM demo.user WHERE lower(username) = lower(%s) AND pass_hash = %s", (credential.username, md5_hash(credential.password)))
        user = cursor.fetchone()

        if user:
            # If the user exists, you can return a token or other authentication mechanism
            # For simplicity, returning a success message here
            return JSONResponse(content={'message': 'Login successful'}, status_code=200)

        return JSONResponse(content={'error': 'Invalid username or password'}, status_code=401)

    except Exception as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)

    finally:
        cursor.close()
        conn.close()


