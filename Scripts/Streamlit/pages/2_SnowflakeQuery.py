# streamlit_app.py
import streamlit as st
import requests

FASTAPI_ENDPOINT = 'http://localhost:8000/query-snowflake/'

st.title('Snowflake Data Viewer')

# User input for SQL query
sql_query = st.text_area("Enter your SQL query:")

if st.button('Execute Query'):
    response = requests.post(FASTAPI_ENDPOINT, json={"sql_query": sql_query})
    if response.status_code == 200:
        data = response.json().get('data')
        st.write(data)
    else:
        st.error(f'Failed to fetch data from Snowflake: {response.text}')


