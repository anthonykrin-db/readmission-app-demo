# response
from typing import List, Optional
#from uuid import str
from api.dao.entities import Response  # assuming that Response model is defined in app.models module
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api.utils.db_utils import get_engine  # Add this function in db_functions.py file

router = APIRouter(tags=["admin -> response"])


class ResponseBase(BaseModel):
  responseid: str
  userid: str
  surveyid: str
  questionid: str
  answers: Optional[str]
  other: Optional[str]
  skipped: Optional[bool]


@router.post("/create") #, response_model=ResponseInDB
def create_response(response: ResponseBase):
  with Session(get_engine()) as db:
    db_response = Response(**response.dict())
    db.add(db_response)
    db.commit()
    db.refresh(db_response)

    return db_response


@router.get("/get/{response_id}") #, response_model=ResponseInDB
def get_response(response_id: str):
  with Session(get_engine()) as db:
    db_response = db.query(Response).get(response_id)
    if db_response is None:
      raise HTTPException(status_code=404, detail="Response not found")

    return db_response


@router.get("/list")  #, response_model=List[ResponseInDB]
def list_responses(skip: int = 0, limit: int = 100):
  with Session(get_engine()) as db:
    responses = db.query(Response).offset(skip).limit(limit).all()
    return responses


@router.put("/update/{response_id}") #, response_model=ResponseInDB
def update_response(response_id: str, response: ResponseBase):
  with Session(get_engine()) as db:
    db_response = db.query(Response).get(response_id)
    if not db_response:
      raise HTTPException(status_code=404, detail="Response not found")

    # update the attributes with those in the request body
    for k, v in response.dict().items():
      setattr(db_response, k, v)

    db.add(db_response)
    db.commit()
    db.refresh(db_response)

    return db_response


@router.delete("/delete/{response_id}")
def delete_response(response_id: str):
  with Session(get_engine()) as db:
    db_response = db.query(Response).get(response_id)
    if not db_response:
      raise HTTPException(status_code=404, detail="Response not found")

    db.delete(db_response)
    db.commit()

  return {"detail": f"Response id {response_id} has been deleted"}
