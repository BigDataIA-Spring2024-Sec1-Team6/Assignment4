# pip install SQLAlchemy snowflake-sqlalchemy snowflake-connector-python
def database_upload_file():

    from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
    import pandas as pd


snowflake_username = 'akshitapathania'
snowflake_password = '***********'
snowflake_account = 'CKMFZWO-AFA59273'
snowflake_database = 'text_extraction'
snowflake_schema = 'public'
snowflake_warehouse = 'text_extraction_wh'

# SQLAlchemy Snowflake connection string
connection_string = f'snowflake://{snowflake_username}:{snowflake_password}@{snowflake_account}/{snowflake_database}?warehouse={snowflake_warehouse}&schema={snowflake_schema}'


# Create SQLAlchemy engine
engine = create_engine(connection_string)

# Define metadata
metadata = MetaData()

# Define the table structure
table_name = 'structured_data'
table = Table(
    table_name,
    metadata,
    Column('id', Integer, primary_key=True),
    Column('topic_name', String),
    Column('year', String),
    Column('level', String),
    Column('introduction_summary', String),
    Column('learning_outcomes', String),
    Column('summary_page_link', String),
    Column('pdf_file_link', String)
)



# Create table in Snowflake if it doesn't exist
if not engine.dialect.has_table(engine, table_name):
    metadata.create_all(engine)


# Function to insert data into Snowflake
def insert_data(data):
    with engine.connect() as conn:
        conn.execute(table.insert().values(data))


# Path to your CSV file
csv_file_path = 'refresher_readings.csv'

# Read data from CSV file
data_from_csv = pd.read_csv(csv_file_path).fillna('')


# Convert DataFrame to list of dictionaries with correct keys
data_to_insert = data_from_csv.rename(columns={
    'Title': 'topic_name',
    'Year': 'year',
    'Level': 'level',
    'Introduction Summary': 'introduction_summary',
    'Learning Outcomes': 'learning_outcomes',
    'Link to Summary Page': 'summary_page_link',
    'Link to PDF File': 'pdf_file_link'
}).to_dict(orient='records')

# Insert data into Snowflake
for data in data_to_insert:
    insert_data(data)

print("Data upload completed.")

#Data upload completed. You can now verify the above upload process by opening the web-based interface of Snowflake, by going into the databases and the table will be displayed there with the uploaded data.

# We can also run Step 5 and 6 commands on the terminal to verify.
