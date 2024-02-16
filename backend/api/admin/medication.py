# medication

from typing import List, Optional
from uuid import UUID
from datetime import date
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api.utils.db_utils import get_engine
from api.dao.entities import Medication

from api.utils.db_utils import get_engine  # Add this function in db_functions.py file

router = APIRouter(tags=["admin -> medication"])


class MedicationBase(BaseModel):
  medicationid: str
  userid: str
  from_dt: Optional[date]
  until_dt: Optional[date]
  label: Optional[str]
  prescription: str
  take_dow_mask: Optional[str]
  dosage_info: Optional[str]
  usage_info: Optional[str]
  warnings_info: Optional[str]


@router.post("/create") #, response_model=Medication
def create_medication(medication: MedicationBase):
  with Session(get_engine()) as db:
    db_medication = Medication(**medication.dict())
    db.add(db_medication)
    db.commit()
    db.refresh(db_medication)
    return db_medication


@router.get("/get/{medication_id}") #, response_model=Medication
def get_medication(medication_id: str):
  with Session(get_engine()) as db:
    db_medication = db.query(Medication).filter(Medication.medicationid == medication_id).first()
    if db_medication is None:
      raise HTTPException(status_code=404, detail="Medication not found")
    return db_medication


@router.get("/list") #, response_model=List[Medication]
def list_medications(skip: int = 0, limit: int = 100):
  with Session(get_engine()) as db:
    medications = db.query(Medication).offset(skip).limit(limit).all()
    return medications


@router.put("/update/{medication_id}") #, response_model=Medication
def update_medication(medication_id: str, medication: MedicationBase):
  with Session(get_engine()) as db:
    db_medication = db.query(Medication).filter(Medication.medicationid == medication_id).first()
    if db_medication is None:
      raise HTTPException(status_code=404, detail="Medication not found")
    for k, v in medication.dict().items():
      setattr(db_medication, k, v)
    db.commit()
    return db_medication


@router.delete("/delete/{medication_id}")
def delete_medication(medication_id: str):
  with Session(get_engine()) as db:
    db_medication = db.query(Medication).filter(Medication.medicationid == medication_id).first()
    if db_medication is None:
      raise HTTPException(status_code=404, detail="Medication not found")
    db.delete(db_medication)
    db.commit()
    return {"detail": f"Medication id {medication_id} has been deleted"}
