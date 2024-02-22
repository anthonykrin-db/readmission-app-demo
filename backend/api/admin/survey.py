# survey
from typing import List, Optional
from uuid import UUID
from datetime import date
from api.dao.entities import Survey  # assuming that Survey model is in app.models module
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel

from sqlalchemy.orm import Session
from api.utils.db_utils import get_engine  # Add this function in db_functions.py file

router = APIRouter(tags=["admin -> survey"])


class SurveyBase(BaseModel):
  surveyid: UUID
  title: str
  description: Optional[str]
  created_dt: Optional[date]
  data: Optional[dict]
  final_msg: Optional[str]


@router.post("/create")  #, response_model=SurveyInDB
def create_survey(survey: SurveyBase):
  with Session(get_engine()) as db:
    db_survey = Survey(**survey.dict())
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)

    return db_survey


@router.get("/get/{survey_id}") #, response_model=SurveyInDB
def get_survey(survey_id: UUID):
  with Session(get_engine()) as db:
    db_survey = db.query(Survey).get(survey_id)
    if db_survey is None:
      raise HTTPException(status_code=404, detail="Survey not found")

    return db_survey


@router.get("/list") #, response_model=List[SurveyInDB]
def list_surveys(skip: int = 0, limit: int = 100):
  with Session(get_engine()) as db:
    surveys = db.query(Survey).offset(skip).limit(limit).all()
    return surveys


@router.put("/update/{survey_id}") #, response_model=SurveyInDB
def update_survey(survey_id: UUID, survey: SurveyBase):
  with Session(get_engine()) as db:
    db_survey = db.query(Survey).get(survey_id)
    if not db_survey:
      raise HTTPException(status_code=404, detail="Survey not found")

    # update the attributes with those in the request body
    for k, v in survey.dict().items():
      setattr(db_survey, k, v)

    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)

    return db_survey


@router.delete("/delete/{survey_id}")
def delete_survey(survey_id: UUID):
  with Session(get_engine()) as db:
    db_survey = db.query(Survey).get(survey_id)
    if not db_survey:
      raise HTTPException(status_code=404, detail="Survey not found")

    db.delete(db_survey)
    db.commit()

  return {"detail": f"Survey id {survey_id} has been deleted"}
