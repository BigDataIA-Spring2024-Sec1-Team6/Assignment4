import streamlit as st
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
import os


# Set up AWS credentials (replace with your own credentials or use environment variables)
# Get AWS credentials from environment variables
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = 'airflowassign'  # Replace with your bucket name

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Streamlit app
st.title('Upload PDF to S3')

uploaded_file = st.file_uploader('Upload a PDF file', type=['pdf'])

if uploaded_file is not None:
    st.write('File uploaded successfully!')

    # Display uploaded file details
    file_details = {'Filename': uploaded_file.name, 'File size': uploaded_file.size}
    st.write(file_details)

    # Save uploaded file to S3
    try:
        s3.upload_fileobj(uploaded_file, AWS_BUCKET_NAME, uploaded_file.name)
        st.success('File saved successfully in S3!')
        st.balloons()
    except NoCredentialsError:
        st.error('AWS credentials not available.')
    except ClientError as e:
        st.error(f'Error uploading file to S3: {e}')
        