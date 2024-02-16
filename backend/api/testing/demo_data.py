# demo_data
from fastapi import APIRouter

from api.testing.data import DemoData

router = APIRouter(tags=["testing -> demo data"])


@router.post("/create")
def create_demo_data():
  # Use the DemoData class to create users
  demo = DemoData()
  demo.create_facilities()
  demo.create_medications()
  demo.create_users()
  demo.create_contact()
  demo.create_survey()
  #demo.create_question()
  #demo.create_response()
  #demo.create_schedule()
  #demo.create_appointments()
  return "Created demo data"
