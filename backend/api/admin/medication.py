# medication

from typing import Optional
from pydantic import BaseModel
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from api.db_utils import get_db  # Add this function in db_functions.py file

router = APIRouter(prefix="/admin/medication", tags=["admin -> medication"])


class MedicationBase(BaseModel):
    userid: UUID
    from_dt: Optional[datetime.date]
    until_dt: Optional[datetime.date]
    label: Optional[str]
    prescription: str
    take_dow_mask: Optional[str]
    dosage_info: Optional[str]
    usage_info: Optional[str]
    warnings_info: Optional[str]

class MedicationCreate(MedicationBase):
    pass

class Medication(MedicationBase):
    medicationid: UUID
    class Config:
        orm_mode = True


app = FastAPI()


@app.post("/medications/", response_model=Medication)
def create_medication(medication: MedicationCreate, db: Session = Depends(get_db)):
    db_medication = Medication(**medication.dict())
    db.add(db_medication)
    db.commit()
    db.refresh(db_medication)
    return db_medication


@app.get("/medications/{medication_id}", response_model=Medication)
def read_medication(medication_id: UUID, db: Session = Depends(get_db)):
    db_medication = db.query(Medication).filter(Medication.medicationid == medication_id).first()
    if db_medication is None:
        raise HTTPException(status_code=404, detail="Medication not found")
    return db_medication


@app.get("/medications/", response_model=List[Medication])
def read_medications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    medications = db.query(Medication).offset(skip).limit(limit).all()
    return medications


@app.put("/medications/{medication_id}", response_model=Medication)
def update_medication(medication_id: UUID, medication: MedicationCreate, db: Session = Depends(get_db)):
    db_medication = db.query(Medication).filter(Medication.medicationid == medication_id).first()
    if db_medication is None:
        raise HTTPException(status_code=404, detail="Medication not found")
    for k, v in medication.dict().items():
        setattr(db_medication, k, v)
    db.commit()
    return db_medication


@app.delete("/medications/{medication_id}")
def delete_medication(medication_id: UUID, db: Session = Depends(get_db)):
    db_medication = db.query(Medication).filter(Medication.medicationid == medication_id).first()
    if db_medication is None:
        raise HTTPException(status_code=404, detail="Medication not found")
    db.delete(db_medication)
    db.commit()
    return {"detail": f"Medication id {medication_id} has been deleted"}