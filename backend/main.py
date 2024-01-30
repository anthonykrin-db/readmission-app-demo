#app.py

from fastapi import FastAPI
from api.health import router as api_health  # import the router we defined in routes.py
from api.auth import router as api_auth  # import the router we defined in routes.py
from api.survey import router as api_survey  # import the router we defined in routes.py


app = FastAPI()

app.include_router(api_health, prefix='/api/monitor')
app.include_router(api_auth, prefix='/api/auth')
app.include_router(api_survey, prefix='/api/survey')
