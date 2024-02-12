from datetime import date
from typing import List
from typing import Optional
from uuid import UUID

from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from api.db_utils import get_engine

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


class UserCreate(UserBase):
  pass


class User(UserBase):
  userid: UUID

  class Config:
    orm_mode = True


@router.post("/create/", response_model=User)
def create_user(user: UserCreate):
  with Session(get_engine()) as db:
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/get/{user_id}", response_model=User)
def get_user(user_id: UUID):
  with Session(get_engine()) as db:
    db_user = db.query(User).filter(User.userid == user_id).first()
    if db_user is None:
      raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/list/", response_model=List[User])
def list_users(skip: int = 0, limit: int = 100):
  with Session(get_engine()) as db:
    db_users = db.query(User).offset(skip).limit(limit).all()
    return db_users


@router.put("/update/{user_id}", response_model=User)
def update_user(user_id: UUID, user: UserCreate):
  with Session(get_engine()) as db:
    db_user = db.query(User).filter(User.userid == user_id).first()
    if db_user is None:
      raise HTTPException(status_code=404, detail="User not found")
    for k, v in user.dict().items():
      setattr(db_user, k, v)
    db.commit()
    return db_user


@router.delete("/delete/{user_id}")
def delete_user(user_id: UUID):
  with Session(get_engine()) as db:
    db_user = db.query(User).filter(User.userid == user_id).first()
    if db_user is None:
      raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"detail": f"User id {user_id} has been deleted"}
