# facility

from typing import List, Optional
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from uuid import UUID
from sqlalchemy.orm import Session
from api.dao.entities import Facility
from api.utils.db_utils import get_engine  # Add this function in db_functions.py file

router = APIRouter(tags=["admin -> facility"])


class FacilityBase(BaseModel):
  facilityid: str
  facility: Optional[str]
  address: Optional[str]
  type: Optional[str]
  logo_url: Optional[str]
  photo_url: Optional[str]


@router.post("/create/") #, response_model=Facility
def create_facility(facility: FacilityBase):
  with Session(get_engine()) as db:
    db_facility = Facility(**facility.dict())
    db.add(db_facility)
    db.commit()
    db.refresh(db_facility)
    return db_facility


@router.get("/get/{facility_id}") #, response_model=FacilityBase
def get_facility(facility_id: str):
  with Session(get_engine()) as db:
    db_facility = db.query(Facility).filter(Facility.facilityid == facility_id).first()
    if db_facility is None:
      raise HTTPException(status_code=404, detail="Facility not found")
    return db_facility


@router.get("/list/") #, response_model=List[Facility]
def list_facilities(skip: int = 0, limit: int = 100):
  with Session(get_engine()) as db:
    facilities = db.query(Facility).offset(skip).limit(limit).all()
    return facilities


@router.put("/update/{facility_id}") #, response_model=Facility
def update_facility(facility_id: str, facility: FacilityBase):
  with Session(get_engine()) as db:
    db_facility = db.query(Facility).filter(Facility.facilityid == facility_id).first()
    if db_facility is None:
      raise HTTPException(status_code=404, detail="Facility not found")
    for k, v in facility.dict().items():
      setattr(db_facility, k, v)
    db.commit()
    return db_facility


@router.delete("/delete/{facility_id}")
def delete_facility(facility_id: str):
  with Session(get_engine()) as db:
    db_facility = db.query(Facility).filter(Facility.facilityid == facility_id).first()
    if db_facility is None:
      raise HTTPException(status_code=404, detail="Facility not found")
    db.delete(db_facility)
    db.commit()
    return {"detail": f"Facility id {facility_id} has been deleted"}
