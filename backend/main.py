#main.py

from fastapi import FastAPI
from api.health import router as api_health  # import the router we defined in routes.py
from api.auth import router as api_auth  # import the router we defined in routes.py
from api.survey import router as api_survey  # import the router we defined in routes.py

from api.admin.activity import router as api_admin_activity
from api.admin.appointment import router as api_admin_appointment
from api.admin.contact import router as api_admin_contact
from api.admin.facility import router as api_admin_facility
from api.admin.medication import router as api_admin_medication
from api.admin.question import router as api_admin_question
from api.admin.response import router as api_admin_response
from api.admin.schedule import router as api_admin_schedule
from api.admin.session import router as api_admin_session
from api.admin.survey import router as api_admin_survey
from api.admin.task import router as api_admin_task
from api.admin.user import router as api_admin_user


app = FastAPI()
# End user facing
app.include_router(api_health, prefix='/api/monitor', tags=["utils -> healthcheck"])
app.include_router(api_auth, prefix='/api/auth', tags=["main -> auth"])
app.include_router(api_survey, prefix='/api/survey', tags=["main -> survey"])


# Admin facing
app.include_router(api_admin_activity, prefix='/api/admin/activity')
app.include_router(api_admin_appointment, prefix='/api/admin/appointment')
app.include_router(api_admin_contact, prefix='/api/admin/contact')
app.include_router(api_admin_facility, prefix='/api/admin/facility')
app.include_router(api_admin_medication, prefix='/api/admin/medication')
app.include_router(api_admin_question, prefix='/api/admin/question')
app.include_router(api_admin_response, prefix='/api/admin/response')
app.include_router(api_admin_schedule, prefix='/api/admin/schedule')
app.include_router(api_admin_session, prefix='/api/admin/session')
app.include_router(api_admin_survey, prefix='/api/admin/survey')
app.include_router(api_admin_task, prefix='/api/admin/task')
app.include_router(api_admin_user, prefix='/api/admin/user')


@app.get("/")
def read_root(): return {"Hello": "World"}
