# task
from typing import List, Optional
from uuid import UUID
from datetime import date
from api.dao.entities import Task  # Assuming that Task model is in app.models module
from fastapi import HTTPException, APIRouter
from pydantic import BaseModel
from sqlalchemy.orm import Session

from api.utils.db_utils import get_engine  # Add this function in db_functions.py file

router = APIRouter(tags=["admin -> task"])


class TaskBase(BaseModel):
  taskid: UUID
  userid: UUID
  type: Optional[str]
  extid: Optional[str]
  due_dt: Optional[date]
  completed_dt: Optional[date]
  status: Optional[str]
  created_dt: Optional[date]
  data: Optional[dict]
  surveyid: Optional[UUID]
  appointmentid: Optional[UUID]
  medicationid: Optional[UUID]
  scheduleid: Optional[UUID]



@router.post("/create") #, response_model=TaskInDB
def create_task(task: TaskBase):
  with Session(get_engine()) as db:
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


@router.get("/get/{task_id}") #, response_model=TaskInDB
def get_task(task_id: UUID):
  with Session(get_engine()) as db:
    db_task = db.query(Task).get(task_id)
    if db_task is None:
      raise HTTPException(status_code=404, detail="Task not found")

    return db_task


@router.get("/list") #, response_model=List[TaskInDB]
def list_tasks(skip: int = 0, limit: int = 100):
  with Session(get_engine()) as db:
    tasks = db.query(Task).offset(skip).limit(limit).all()
    return tasks


@router.put("/update/{task_id}") #, response_model=TaskInDB
def update_task(task_id: UUID, task: TaskBase):
  with Session(get_engine()) as db:
    db_task = db.query(Task).get(task_id)
    if not db_task:
      raise HTTPException(status_code=404, detail="Task not found")

    # update the attributes with those in the request body
    for k, v in task.dict().items():
      setattr(db_task, k, v)

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


@router.delete("/delete/{task_id}")
def delete_task(task_id: UUID):
  with Session(get_engine()) as db:
    db_task = db.query(Task).get(task_id)
    if not db_task:
      raise HTTPException(status_code=404, detail="Task not found")

    db.delete(db_task)
    db.commit()

  return {"detail": f"Task id {task_id} has been deleted"}
