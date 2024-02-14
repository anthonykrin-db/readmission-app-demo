from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from api.utils.db_utils import get_engine
from api.utils.misc_utils import md5_hash
from sqlalchemy.orm import Session
from api.dao.entities import Users
from sqlalchemy import and_
import time
from typing import Dict
import jwt
import os
from dotenv import load_dotenv

load_dotenv()  # Loads environment variables from .env file

JWT_SECRET = os.environ.get("JWT_SECRET")
JWT_ALGORITHM = os.environ.get("JWT_ALGO")

router = APIRouter()


# Class for credential
class Credential(BaseModel):
  username: str
  password: str


@router.post('/login')
async def login(credential: Credential):
  if not credential.username or not credential.password:
    return JSONResponse(content={'error': 'Username and password are required'}, status_code=400)

  try:
    with Session(get_engine()) as db:
      db_user = db.query(Users).filter(and_(Users.username==credential.username, Users.pass_hash == md5_hash(credential.password))).first()

      if db_user is None:
        # If the user exists, you can return a token or other authentication mechanism
        # For simplicity, returning a success message here
        return JSONResponse(content={'error': 'Invalid username or password'}, status_code=401)
      jwttoken = signJWT(str(db_user.userid), db_user.username)
      return JSONResponse(content={'message': 'Login successful','token':jwttoken}, status_code=200)

  except Exception as e:
    return JSONResponse(content={'error': str(e)}, status_code=500)

def signJWT(userid: str,username:str) -> Dict[str, str]:
  payload = {
    "userid": userid,
    "username": username,
    "expires": time.time() + 600
  }
  token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

  return token

def decodeJWT(token: str) -> dict:
  try:
    decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
    return decoded_token if decoded_token["expires"] >= time.time() else None
  except:
    return {}
