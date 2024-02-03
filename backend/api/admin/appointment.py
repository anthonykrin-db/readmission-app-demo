from typing import Optional
from pydantic import BaseModel
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from api.db_utils import get_db  # Add this function in db_functions.py file

router = APIRouter(prefix="/admin/appointment", tags=["admin -> appointment"])


class AppointmentBase(BaseModel):
    userid: UUID
    start_date: datetime.date
    end_date: Optional[datetime.date]
    location: Optional[str]
    physician: Optional[str]
    reason: Optional[str]
    reason_es: Optional[str]
    confirmed: bool = False
    confirmed_dt: Optional[datetime.date]
    reschedule_phone: Optional[str]
    cancelled: bool = False
    cancelled_dt: Optional[datetime.date]
    days_reminder: int = 0

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    appointmentid: UUID
    class Config:
        orm_mode = True


app = FastAPI()


@app.post("/create/", response_model=Appointment)
def create_appointment(appointment: AppointmentCreate, db: Session = Depends(get_db)):
    db_appointment = Appointment(**appointment.dict())
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment


@app.get("/get/{appointment_id}", response_model=Appointment)
def read_appointment(appointment_id: UUID, db: Session = Depends(get_db)):
    db_appointment = db.query(Appointment).filter(Appointment.appointmentid == appointment_id).first()
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return db_appointment


@app.get("/list/", response_model=List[Appointment])
def read_appointments(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    appointments = db.query(Appointment).offset(skip).limit(limit).all()
    return appointments


@app.put("/update/{appointment_id}", response_model=Appointment)
def update_appointment(appointment_id: UUID, appointment: AppointmentCreate, db: Session = Depends(get_db)):
    db_appointment = db.query(Appointment).filter(Appointment.appointmentid == appointment_id).first()
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    for k, v in appointment.dict().items():
        setattr(db_appointment, k, v)
    db.commit()
    return db_appointment


@app.delete("/delete/{appointment_id}")
def delete_appointment(appointment_id: UUID, db: Session = Depends(get_db)):
    db_appointment = db.query(Appointment).filter(Appointment.appointmentid == appointment_id).first()
    if db_appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    db.delete(db_appointment)
    db.commit()
    return {"detail": f"Appointment id {appointment_id} has been deleted"}
