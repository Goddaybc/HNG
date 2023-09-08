from fastapi import FastAPI
from datetime import datetime
from typing import Optional

app = FastAPI()


@app.get('/')
def index():
    return {"Hello": "World"}


@app.get("/api")
def get_data(slack_name: Optional[str] = None, track: Optional[str] = None):
    if slack_name is None or track is None:
        return {"error": "Both slack_name and track parameters are required"}

    # Get the current day of the week in full
    current_day = datetime.now().strftime("%A")

    # Get the current UTC time with a +/-2 minute window
    current_utc_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Github repository information
