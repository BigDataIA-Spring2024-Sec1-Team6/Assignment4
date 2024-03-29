from airflow import DAG

from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime, timedelta
import requests
#from tasks.download_from_s3 import begin_download
#from tasks.trigger_grobid import grobid_process
#from tasks import content_parser



import os
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta 
from Callables.metadata_extraction import metadata_extraction_file
from Callables.metadata_class import metadata_class_file
from Callables.database_upload import database_upload_file
from Callables.content_extraction import content_extraction_file
from Callables.Content_class import content_class_file
from Callables.grobid.grobid_extraction_file1 import grobid_extraction_file1
from Callables.grobid.grobid_extraction_file2 import grobid_extraction_file2
from Callables.grobid.grobid_extraction_file3 import grobid_extraction_file3




S3_BUCKET_NAME = 'airflowassign'

with DAG(
    dag_id='EVD_master',
    default_args={'start_date': days_ago(1),
    'execution_timeout': timedelta(minutes=30)},
    schedule_interval='0 23 * * *',
    catchup=False
) as dag:

    grobid_extraction_file1 = PythonOperator(
        task_id='grobid_extraction_file1',
        python_callable=grobid_extraction_file1
        dag=dag
    )

    grobid_extraction_file2 = PythonOperator(
        task_id='grobid_extraction_file2',
        python_callable=grobid_extraction_file2,
        dag=dag
    )

    grobid_extraction_file3 = PythonOperator(
        task_id='grobid_extraction_file3',
        python_callable=grobid_extraction_file3,
        dag=dag
    )

with dag:
    content_extraction = PythonOperator(
        task_id='content_extraction',
        python_callable=content_extraction_file,
        
    )
    
with dag:
    metadata_extraction = PythonOperator(
        task_id='metadata_extraction',
        python_callable=metadata_extraction_file,
        
    )
    

with dag:
    content_class = PythonOperator(
        task_id='content_validation',
        python_callable=content_class_file,
        
    )
    
with dag:
    metadata_class = PythonOperator(
        task_id='metadata_validation',
        python_callable=metadata_class_file,
        
    )

with dag:
    database_upload = Stagingoperator(
        task_id='database_upload',
        python_callable=database_upload_file,
    )
    
    
#Step to create dependencies, in a parallel fashion we set grobid extraction files, then content and metadata extraction with class files and data upload in snowflake.
grobid_extraction_file1 >> content_extraction_file >> metadata_extraction_file
grobid_extraction_file2 >> content_extraction_file >> metadata_extraction_file
grobid_extraction_file3 >> content_extraction_file >> metadata_extraction_file


metadata_extraction_file >> metadata_class_file
content_extraction_file >> content_class_file


metadata_class_file >> database_upload_file
content_class_file >> database_upload_file