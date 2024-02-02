from fastapi import APIRouter
from api.db_utils import md5_hash,get_database_session
from pydantic import BaseModel
from fastapi.responses import JSONResponse

######################################################
# Admin only crud.  This should not be public facing
######################################################


# activities
router = APIRouter(prefix="/admin/activities", tags=["activities"])

class ActivityEntity(BaseModel):
    activityid: UUID4
    type: str
    occurence_dt: str  # Assuming the date is provided as a string, you can adjust this based on your needs
    extid: str
    label: str
    description: str
    icon: str


@router.get("/activities", response_model=List[ActivityEntity])
async def list_activities(db: Session = Depends(get_database_session)):
    """
    Retrieve a list of activities.
    """
    activities = db.query(ActivityEntity).all()
    return activities

@router.post("/", response_model=ActivityResponse)
async def create_activity(activity: ActivityEntity, db: Session = Depends(get_database_session)):
    #TODO: overwrite guid
    db_activity = Activity(**activity.dict())
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity


@router.get("/{activity_id}", response_model=ActivityEntity)
async def get_activity(activity_id: UUID4, db: Session = Depends(get_database_session)):
    """
    Retrieve a particular activity by its activityid.
    """
    activity = db.query(ActivityEntity).filter(ActivityEntity.activityid == activity_id).first()
    if activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return activity
