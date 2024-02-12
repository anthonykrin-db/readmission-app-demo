from pydantic import BaseModel


######################################################
# Admin only crud.  This should not be public facing
######################################################

class Result(BaseModel):
  success: bool
  msg: str
