from datetime import date
from typing import List, Optional
from uuid import UUID
from datetime import date
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from api.db_utils import get_engine

router = APIRouter(tags=["admin -> appointment"])


##app = FastAPI()

class AppointmentBase(BaseModel):
  userid: UUID
  start_date: date
  end_date: Optional[date]
  location: Optional[str]
  physician: Optional[str]
  reason: Optional[str]
  reason_es: Optional[str]
  confirmed: bool = False
  confirmed_dt: Optional[date]
  reschedule_phone: Optional[str]
  cancelled: bool = False
  cancelled_dt: Optional[date]
  days_reminder: int = 0


class AppointmentCreate(AppointmentBase):
  pass


class Appointment(AppointmentBase):
  appointmentid: UUID

  class Config:
    orm_mode = True


# app = FastAPI()


@router.post("/create", response_model=Appointment)
def create_appointment(appointment: AppointmentCreate):
  with Session(get_engine()) as db:
    db_appointment = Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


@router.get("/get/{appointment_id}", response_model=Appointment)
def read_appointment(appointment_id: UUID):
  with Session(get_engine()) as db:
    db_appointment = db.query(Appointment).filter(Appointment.appointmentid == appointment_id).first()
    if db_appointment is None:
      raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment


@router.get("/list/", response_model=List[Appointment])
def read_appointments(skip: int = 0, limit: int = 100):
  with Session(get_engine()) as db:
    appointments = db.query(Appointment).offset(skip).limit(limit).all()
    return appointments


@router.put("/update/{appointment_id}", response_model=Appointment)
def update_appointment(appointment_id: UUID, appointment: AppointmentCreate):
  with Session(get_engine()) as db:
    db_appointment = db.query(Appointment).filter(Appointment.appointmentid == appointment_id).first()
    if db_appointment is None:
      raise HTTPException(status_code=404, detail="Appointment not found")
    for k, v in appointment.dict().items():
      setattr(db_appointment, k, v)
    db.commit()
    return db_appointment


@router.delete("/delete/{appointment_id}")
def delete_appointment(appointment_id: UUID):
  with Session(get_engine()) as db:
    db_appointment = db.query(Appointment).filter(Appointment.appointmentid == appointment_id).first()
    if db_appointment is None:
      raise HTTPException(status_code=404, detail="Appointment not found")
    db.delete(db_appointment)
    db.commit()
    return {"detail": f"Appointment id {appointment_id} has been deleted"}
