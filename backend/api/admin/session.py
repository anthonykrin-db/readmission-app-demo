# session
from typing import List, Optional
from uuid import UUID
from datetime import date
from api.dao.entities import Session  # assuming Session model is in app.models module
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from api.db_utils import get_engine  # Add this function in db_functions.py file

router = APIRouter(tags=["admin -> session"])


class SessionBase(BaseModel):
  sessionid: UUID
  userid: UUID
  login_dt: Optional[date]
  exp_dt: Optional[date]


class SessionCreate(SessionBase):
  pass


class SessionInDB(SessionBase):
  sessionid: UUID

  class Config:
    orm_mode = True


@router.post("/create", response_model=SessionInDB)
def create_session(session: SessionCreate):
  with Session(get_engine()) as db:
    db_session = Session(**session.dict())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)

    return db_session


@router.get("/get/{session_id}", response_model=SessionInDB)
def read_session(session_id: UUID):
  with Session(get_engine()) as db:
    db_session = db.query(Session).get(session_id)
    if db_session is None:
      raise HTTPException(status_code=404, detail="Session not found")

    return db_session


@router.get("/list", response_model=List[SessionInDB])
def read_sessions(skip: int = 0, limit: int = 100):
  with Session(get_engine()) as db:
    sessions = db.query(Session).offset(skip).limit(limit).all()
    return sessions


@router.put("/update/{session_id}", response_model=SessionInDB)
def update_session(session_id: UUID, session: SessionCreate):
  with Session(get_engine()) as db:
    db_session = db.query(Session).get(session_id)
    if not db_session:
      raise HTTPException(status_code=404, detail="Session not found")

    # update the attributes with those in the request body
    for k, v in session.dict().items():
      setattr(db_session, k, v)

    db.add(db_session)
    db.commit()
    db.refresh(db_session)

    return db_session


@router.delete("/delete/{session_id}")
def delete_session(session_id: UUID):
  with Session(get_engine()) as db:
    db_session = db.query(Session).get(session_id)
    if not db_session:
      raise HTTPException(status_code=404, detail="Session not found")

    db.delete(db_session)
    db.commit()

  return {"detail": f"Session id {session_id} has been deleted"}
