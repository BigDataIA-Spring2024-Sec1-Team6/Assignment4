# fastapi_snowflake.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import snowflake.connector
import warnings
from dotenv import load_dotenv
import os
load_dotenv()

warnings.filterwarnings("ignore")

class Query(BaseModel):
    sql_query: str

app = FastAPI()

# Snowflake connection parameters
SNOWFLAKE_ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
SNOWFLAKE_USER = os.getenv("SNOWFLAKE_USER")
SNOWFLAKE_PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
SNOWFLAKE_WAREHOUSE = os.getenv("SNOWFLAKE_WAREHOUSE")
SNOWFLAKE_DATABASE = os.getenv('SNOWFLAKE_DATABASE')
SNOWFLAKE_SCHEMA = os.getenv('SNOWFLAKE_SCHEMA')

@app.post("/query-snowflake/")
def query_snowflake(query: Query):
    try:
        conn = snowflake.connector.connect(
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT,
            warehouse=SNOWFLAKE_WAREHOUSE,
            database=SNOWFLAKE_DATABASE,
            schema=SNOWFLAKE_SCHEMA
        )
        cursor = conn.cursor()
        cursor.execute(query.sql_query)
        result = cursor.fetchall()
        return {"data": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

