# demo_data
from fastapi import APIRouter

from api.testing.data import DemoData

router = APIRouter(tags=["testing -> demo data"])


@router.post("/create")
def create_demo_data():
  # Use the DemoData class to create users
  demo = DemoData()
  demo.create_users()
  demo.print_users()
  return "Created demo data"
