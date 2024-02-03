# facility

from typing import Optional
from pydantic import BaseModel
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException
from api.db_utils import get_db  # Add this function in db_functions.py file

router = APIRouter(prefix="/admin/facility", tags=["admin -> facility"])


class FacilityBase(BaseModel):
    facility: Optional[str]
    address: Optional[str]
    type: Optional[str]
    logo_url: Optional[str]
    photo_url: Optional[str]

class FacilityCreate(FacilityBase):
    pass

class Facility(FacilityBase):
    facilityid: UUID
    class Config:
        orm_mode = True


app = FastAPI()


@app.post("/facilities/", response_model=Facility)
def create_facility(facility: FacilityCreate, db: Session = Depends(get_db)):
    db_facility = Facility(**facility.dict())
    db.add(db_facility)
    db.commit()
    db.refresh(db_facility)
    return db_facility


@app.get("/facilities/{facility_id}", response_model=Facility)
def read_facility(facility_id: UUID, db: Session = Depends(get_db)):
    db_facility = db.query(Facility).filter(Facility.facilityid == facility_id).first()
    if db_facility is None:
        raise HTTPException(status_code=404, detail="Facility not found")
    return db_facility


@app.get("/facilities/", response_model=List[Facility])
def read_facilities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    facilities = db.query(Facility).offset(skip).limit(limit).all()
    return facilities


@app.put("/facilities/{facility_id}", response_model=Facility)
def update_facility(facility_id: UUID, facility: FacilityCreate, db: Session = Depends(get_db)):
    db_facility = db.query(Facility).filter(Facility.facilityid == facility_id).first()
    if db_facility is None:
        raise HTTPException(status_code=404, detail="Facility not found")
    for k, v in facility.dict().items():
        setattr(db_facility, k, v)
    db.commit()
    return db_facility


@app.delete("/facilities/{facility_id}")
def delete_facility(facility_id: UUID, db: Session = Depends(get_db)):
    db_facility = db.query(Facility).filter(Facility.facilityid == facility_id).first()
    if db_facility is None:
        raise HTTPException(status_code=404, detail="Facility not found")
    db.delete(db_facility)
    db.commit()
    return {"detail": f"Facility id {facility_id} has been deleted"}
