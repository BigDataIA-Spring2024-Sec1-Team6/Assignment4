from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class S3FileLocation(BaseModel):
    s3_file_location: str

# Replace with your actual Airflow endpoint and credentials
AIRFLOW_API_ENDPOINT = "http://localhost:8080/api/v1/dags/osborne_dag/dagRuns"
AIRFLOW_USERNAME = "airflow"
AIRFLOW_PASSWORD = "airflow"

@app.post("/trigger-airflow/")
def trigger_airflow(file_location: S3FileLocation):
    airflow_payload = {
        "conf": {
            "s3_file_location": file_location.s3_file_location
        }
    }
    
    response = requests.post(
        AIRFLOW_API_ENDPOINT,
        json=airflow_payload,
        auth=(AIRFLOW_USERNAME, AIRFLOW_PASSWORD)
    )
    
    return {"airflow_response": response.json()}
