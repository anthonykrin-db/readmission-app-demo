# contact
from typing import Optional
from pydantic import BaseModel
from datetime import date
from typing import List
from uuid import UUID
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter
from api.db_utils import get_db  # Add this function in db_functions.py file

router = APIRouter(tags=["admin -> contact"])
##app = FastAPI()

class ContactBase(BaseModel):
    userid: UUID
    contact_extid: Optional[str]
    contact_label: Optional[str]

class ContactCreate(ContactBase):
    pass

class Contact(ContactBase):
    contactid: UUID
    class Config:
        orm_mode = True


@router.post("/create/", response_model=Contact)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


@router.get("/get/{contact_id}", response_model=Contact)
def read_contact(contact_id: UUID, db: Session = Depends(get_db)):
    db_contact = db.query(Contact).filter(Contact.contactid == contact_id).first()
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return db_contact


@router.get("/list/", response_model=List[Contact])
def read_contacts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    contacts = db.query(Contact).offset(skip).limit(limit).all()
    return contacts


@router.put("/update/{contact_id}", response_model=Contact)
def update_contact(contact_id: UUID, contact: ContactCreate, db: Session = Depends(get_db)):
    db_contact = db.query(Contact).filter(Contact.contactid == contact_id).first()
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    for k, v in contact.dict().items():
        setattr(db_contact, k, v)
    db.commit()
    return db_contact


@router.delete("/delete/{contact_id}")
def delete_contact(contact_id: UUID, db: Session = Depends(get_db)):
    db_contact = db.query(Contact).filter(Contact.contactid == contact_id).first()
    if db_contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    db.delete(db_contact)
    db.commit()
    return {"detail": f"Contact id {contact_id} has been deleted"}
