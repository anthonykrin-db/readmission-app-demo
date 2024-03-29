from datetime import date
from typing import List
from typing import Optional
from uuid import UUID
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session
from api.utils.db_utils import get_engine
from api.dao.entities import Users

router = APIRouter(tags=["admin -> users"])


class UserBase(BaseModel):
  userid: str
  type: str
  is_patient: bool
  first_name: str
  last_name: str
  patientid: Optional[str]
  pass_hash: Optional[str]
  last_login_dt: Optional[date]
  contact_information: Optional[str]
  other_information: Optional[str]
  extid: Optional[str]
  department: Optional[str]
  location: Optional[str]
  suffix: Optional[str]
  prefix: Optional[str]
  affiliated_facilityid: Optional[UUID]
  photo_url: Optional[str]
  username: str

@router.post("/create/") #, response_model=Users
def create_user(user: UserBase):
  with Session(get_engine()) as db:
    db_user = Users(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/get/{user_id}") #, response_model=Users
def get_user(user_id: str):
  with Session(get_engine()) as db:
    db_user = db.query(Users).filter(Users.userid == user_id).first()
    if db_user is None:
      raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/list/") #, response_model=List[Users]
def list_users(skip: int = 0, limit: int = 100):
  with Session(get_engine()) as db:
    db_users = db.query(Users).offset(skip).limit(limit).all()
    return db_users


@router.put("/update/{user_id}") #, response_model=Users
def update_user(user_id: UUID, user: UserBase):
  with Session(get_engine()) as db:
    db_user = db.query(Users).filter(Users.userid == user_id).first()
    if db_user is None:
      raise HTTPException(status_code=404, detail="User not found")
    for k, v in user.dict().items():
      setattr(db_user, k, v)
    db.commit()
    return db_user


@router.delete("/delete/{user_id}")
def delete_user(user_id: str):
  with Session(get_engine()) as db:
    db_user = db.query(Users).filter(Users.userid == user_id).first()
    if db_user is None:
      raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"detail": f"User id {user_id} has been deleted"}
