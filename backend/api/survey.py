from fastapi import APIRouter

router = APIRouter()

@router.get("/suvey/")
def healthcheck():
    return 'Survey place holder'
