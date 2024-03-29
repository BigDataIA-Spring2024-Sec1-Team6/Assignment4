import streamlit as st
import requests
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import os

# Set up AWS credentials
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = 'airflowassign'  # Replace with your bucket name

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Streamlit app
st.title('PDF Processing on S3')

# List files from S3 bucket
try:
    objects = s3.list_objects_v2(Bucket=AWS_BUCKET_NAME)
    if 'Contents' in objects:
        file_names = [obj['Key'] for obj in objects['Contents'] if obj['Key'].endswith('.pdf')]
        xml_files = [obj['Key'] for obj in objects['Contents'] if obj['Key'].endswith('.xml')]

        # Extraction process
        st.subheader('Extraction Validation and Loading')
        selected_pdf = st.selectbox('Select a PDF file to extract', file_names)
        if st.button('Start Airflow'):
            extraction_endpoint = f"http://localhost:8000/process_s3_file/{selected_pdf}"
            response = requests.get(extraction_endpoint)
            if response.status_code == 200:
                st.success('Airflow started successfully!')
            else:
                st.error(f'Airflow failed: {response.text}')
    else:
        st.write('No files found in the bucket.')
except NoCredentialsError:
    st.error('AWS credentials not available.')
except ClientError as e:
    st.error(f'Error fetching files from S3: {e}')