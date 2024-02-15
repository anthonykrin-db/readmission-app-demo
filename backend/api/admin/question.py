# question
from typing import List, Optional
from uuid import UUID
from api.dao.entities import Question  # assuming that Question model is defined in app.models module
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from api.utils.db_utils import get_engine  # Add this function in db_functions.py file

router = APIRouter(tags=["admin -> question"])


class QuestionBase(BaseModel):
  questionid: UUID
  surveyid: UUID
  type: str
  question: str
  responses: Optional[str]
  data: Optional[dict]
  multiple_choice: Optional[bool]
  has_other: Optional[bool]
  other_label: Optional[str]
  sequence: Optional[int]


class QuestionCreate(QuestionBase):
  pass


class QuestionInDB(QuestionBase):
  questionid: UUID

  class Config:
    orm_mode = True


@router.post("/create", response_model=QuestionInDB)
def create_question(question: QuestionCreate):
  with Session(get_engine()) as db:
    db_question = Question(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    return db_question


@router.get("/get/{question_id}", response_model=QuestionInDB)
def get_question(question_id: UUID):
  with Session(get_engine()) as db:
    db_question = db.query(Question).get(question_id)
    if db_question is None:
      raise HTTPException(status_code=404, detail="Question not found")

    return db_question


@router.get("/list", response_model=List[QuestionInDB])
def list_questions(skip: int = 0, limit: int = 100):
  with Session(get_engine()) as db:
    questions = db.query(Question).offset(skip).limit(limit).all()
    return questions


@router.put("/update/{question_id}", response_model=QuestionInDB)
def update_question(question_id: UUID, question: QuestionCreate):
  with Session(get_engine()) as db:
    db_question = db.query(Question).get(question_id)
    if not db_question:
      raise HTTPException(status_code=404, detail="Question not found")

    # update the attributes with those in the request body
    for k, v in question.dict().items():
      setattr(db_question, k, v)

    db.add(db_question)
    db.commit()
    db.refresh(db_question)

    return db_question


@router.delete("/delete/{question_id}")
def delete_question(question_id: UUID):
  with Session(get_engine()) as db:
    db_question = db.query(Question).get(question_id)
    if not db_question:
      raise HTTPException(status_code=404, detail="Question not found")

    db.delete(db_question)
    db.commit()

  return {"detail": f"Question id {question_id} has been deleted"}
