# schedule
from typing import List, Optional
from uuid import UUID
from datetime import date
from api.dao.entities import Schedule  # assuming Schedule model is in app.models module
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from api.db_utils import get_engine  # Add this function in db_functions.py file

router = APIRouter(tags=["admin -> schedule"])


class ScheduleBase(BaseModel):
  scheduleid: UUID
  label: str
  type: str
  userid: UUID
  dow_mask: Optional[str]
  start_dt: Optional[date]
  end_dt: Optional[date]
  repeats: Optional[bool]
  data: Optional[dict]


class ScheduleCreate(ScheduleBase):
  pass


class ScheduleInDB(ScheduleBase):
  scheduleid: UUID

  class Config:
    orm_mode = True


@router.post("/create", response_model=ScheduleInDB)
def create_schedule(schedule: ScheduleCreate):
  with Session(get_engine()) as db:
    db_schedule = Schedule(**schedule.dict())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)

    return db_schedule


@router.get("/get/{schedule_id}", response_model=ScheduleInDB)
def read_schedule(schedule_id: UUID):
  with Session(get_engine()) as db:
    db_schedule = db.query(Schedule).get(schedule_id)
    if db_schedule is None:
      raise HTTPException(status_code=404, detail="Schedule not found")

    return db_schedule


@router.get("/list", response_model=List[ScheduleInDB])
def read_schedules(skip: int = 0, limit: int = 100):
  with Session(get_engine()) as db:
    schedules = db.query(Schedule).offset(skip).limit(limit).all()
    return schedules


@router.put("/update/{schedule_id}", response_model=ScheduleInDB)
def update_schedule(schedule_id: UUID, schedule: ScheduleCreate):
  with Session(get_engine()) as db:
    db_schedule = db.query(Schedule).get(schedule_id)
    if not db_schedule:
      raise HTTPException(status_code=404, detail="Schedule not found")

    # update the attributes with those in the request body
    for k, v in schedule.dict().items():
      setattr(db_schedule, k, v)

    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)

    return db_schedule


@router.delete("/delete/{schedule_id}")
def delete_schedule(schedule_id: UUID):
  with Session(get_engine()) as db:
    db_schedule = db.query(Schedule).get(schedule_id)
    if not db_schedule:
      raise HTTPException(status_code=404, detail="Schedule not found")

    db.delete(db_schedule)
    db.commit()

  return {"detail": f"Schedule id {schedule_id} has been deleted"}
