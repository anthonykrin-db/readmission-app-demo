# demo_data
from fastapi import APIRouter
from api.auth.auth_handler import signJWT

router = APIRouter(tags=["testing -> jwt tokens"])

@router.get("/generate-token/{user_id}/{username}",response_model=str)
def generate_token(user_id: str, username: str):
  jwttoken = signJWT(str(user_id), username)
  return jwttoken
