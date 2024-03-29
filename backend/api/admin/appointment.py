from datetime import date
from typing import Optional
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api.dao.entities import Appointment
from api.utils.db_utils import get_engine

router = APIRouter(tags=["admin -> appointment"])

class AppointmentBase(BaseModel):
  appointmentid: str
  userid: str
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


@router.post("/create")  # , response_model=Appointment
def create_appointment(appointment: AppointmentBase):
  with Session(get_engine()) as db:
    db_appointment = AppointmentBase(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


@router.get("/get/{appointment_id}")  # , response_model=Appointment
def get_appointment(appointment_id: str):
  with Session(get_engine()) as db:
    db_appointment = db.query(Appointment).filter(Appointment.appointmentid == appointment_id).first()
    if db_appointment is None:
      raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment


@router.get("/list/")  # , response_model=List[Appointment]
def list_appointments(skip: int = 0, limit: int = 100):
  with Session(get_engine()) as db:
    appointments = db.query(Appointment).offset(skip).limit(limit).all()
    return appointments


@router.put("/update/{appointment_id}")  # , response_model=Appointment
def update_appointment(appointment_id: str, appointment: AppointmentBase):
  with Session(get_engine()) as db:
    db_appointment = db.query(Appointment).filter(Appointment.appointmentid == appointment_id).first()
    if db_appointment is None:
      raise HTTPException(status_code=404, detail="Appointment not found")
    for k, v in appointment.dict().items():
      setattr(db_appointment, k, v)
    db.commit()
    return db_appointment


@router.delete("/delete/{appointment_id}")
def delete_appointment(appointment_id: str):
  with Session(get_engine()) as db:
    db_appointment = db.query(Appointment).filter(Appointment.appointmentid == appointment_id).first()
    if db_appointment is None:
      raise HTTPException(status_code=404, detail="Appointment not found")
    db.delete(db_appointment)
    db.commit()
    return {"detail": f"Appointment id {appointment_id} has been deleted"}
