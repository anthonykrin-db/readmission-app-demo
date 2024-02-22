from fastapi import Depends
from fastapi import HTTPException, APIRouter, Request
from sqlalchemy.orm import Session
from api.auth.auth_bearer import JWTBearer
from api.dao.entities import Survey
from api.utils.db_utils import get_engine  # Add this function in db_functions.py file
from uuid import UUID

router = APIRouter()


# Requires authentication

@router.get("/survey/{survey_id}", dependencies=[Depends(JWTBearer())], tags=[])
def get_survey(survey_id: UUID, request: Request):
  # getting survey for user..
  print("credentials: {}".format(request.state.credentials))

  with Session(get_engine()) as db:
    # TODO: get more data from survey
    db_survey = db.query(Survey).get(survey_id)
    if db_survey is None:
      raise HTTPException(status_code=404, detail="Survey not found")

    return db_survey
