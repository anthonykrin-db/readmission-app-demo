# task
from fastapi import APIRouter, Depends
from api.db_utils import get_db
from datetime import date
from api.misc_utils import md5_hash,generate_guid
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import UUID
from typing import List
from api.dao.entities import Activity

######################################################
# Admin only crud.  This should not be public facing
######################################################

router = APIRouter(tags=["admin -> task"])
#app = FastAPI()


