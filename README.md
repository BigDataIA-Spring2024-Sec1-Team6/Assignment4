# Assignment4

## Problem Statement 

Develop an automated data processing pipeline to extract content and metadata from PDF files, validate the data, and load it into a Snowflake database, enabling query responses through a web application.

## Project Goals

1. **Automate PDF Data Handling**: Create a reliable, automated pipeline for extracting and processing data from PDF files.
2. **Integrate Cloud Storage and Processing**: Use AWS S3 for storage and Airflow for orchestrating the pipeline.
3. **Implement Data Validation**: Ensure data quality through validation checks before loading into the database.
4. **Develop API Services**: Build APIs for data processing and database querying.
5. **Facilitate User Interaction**: Design a user-friendly interface using Streamlit for file uploads and data retrieval.
6. **Ensure Accessibility**: The entire process should be accessible online, with no local dependency.
7. **Containerization and Deployment**: Dockerize the components and host them online to ensure scalability and ease of deployment.
8. **Documentation and Version Control**: Provide thorough documentation and maintain code with GitHub.

## Technologies Used

![Airflow](https://img.shields.io/badge/Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Snowflake](https://img.shields.io/badge/Snowflake-29B5E8?style=for-the-badge&logo=snowflake&logoColor=white)
![AWS S3](https://img.shields.io/badge/AWS_S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![Google Codelabs](https://img.shields.io/badge/Google_Codelabs-4285F4?style=for-the-badge&logo=google&logoColor=white)


## Data Sources

2. **PDF Documents**: These are the three PDF files given.
3. **CSV Files**: Data files generated after processing PDF documents and webpages, containing structured information ready to be loaded into Snowflake.
4. **Grobid Output**: The result of processing the three PDF files through the Grobid tool, as .txt files, representing extracted data.
5. **Snowflake Datasets**: Pre-existing datasets within Snowflake used for validation or augmentation of the extracted data.
6.  **AWS Services**: (**S3 Buckets**) Raw and processed data storage.

## Pre requisites

The prerequisites for undertaking the described project would likely include:

1. **API Development with FastAPI**: Proficiency in developing robust APIs with FastAPI, including route creation, request handling, and response formatting.
2. **Data Orchestration with Airflow**: Familiarity with Airflow for workflow orchestration, including creating DAGs, operators, and understanding task dependencies.
3. **Streamlit Web Application**: Experience in building interactive web applications using Streamlit, integrating backend services, and managing user inputs.
4. **AWS Services**: Understanding of AWS services, particularly S3 for file storage and operations.
5. **Containerization with Docker**: Practical knowledge of creating, managing, and deploying Docker containers for application and environment encapsulation.
6. **Version Control with GitHub**: Experience with Git for version control, including committing changes, merging branches, and resolving conflicts on GitHub.
7. **Documentation with Google Codelabs**: Ability to create informative and clear documentation using Google Codelabs, providing step-by-step guides and explanations.

## Project Structure

```
📦 
├─ .gitignore
├─ Diagrams
│  ├─ ArchDiag.png
│  └─ ArchDiagram.txt
├─ PDF_Files.txt
│  ├─ 2024-l1-topics-combined-2.pdf
│  ├─ 2024-l2-topics-combined-2.pdf
│  └─ 2024-l3-topics-combined-2.pdf
├─ README.md
├─ Scripts
│  ├─ Airflow
│  │  ├─ Callables
│  │  │  ├─ .env
│  │  │  ├─ Content_class.py
│  │  │  ├─ content_extraction.py
│  │  │  ├─ database_upload.py
│  │  │  ├─ grobid
│  │  │  │  ├─ grobid_extraction_file1.py
│  │  │  │  ├─ grobid_extraction_file2.py
│  │  │  │  ├─ grobid_extraction_file3.py
│  │  │  │  └─ roughtwork.txt
│  │  │  ├─ grobid_test.py
│  │  │  ├─ metadata_class.py
│  │  │  └─ metadata_extraction.py
│  │  ├─ dags
│  │  │  └─ master_dag.py
│  │  ├─ docker-compose.yaml
│  │  ├─ logs
│  │  └─ requirements.txt
│  ├─ FastAPI
│  │  ├─ FastAPI1_TriggerAirflow.py
│  │  ├─ FastAPI2_SnowflakeConnection.py
│  │  └─ requirements.txt
│  └─ Streamlit
│     ├─ Dockerfile
│     ├─ docker-compose.yaml
│     ├─ home.py
│     ├─ pages
│     │  ├─ 1_Extraction&Validation&Loading.py
│     │  └─ 2_SnowflakeQuery.py
│     └─ requirements.txt
└─ requirements.txt
```



## References 
- https://grobid.readthedocs.io/en/latest/Run-Grobid/
- https://docs.getdbt.com/guides/snowflake?step=1
- https://diagrams.mingrammer.com/docs/guides/diagram
- https://docs.streamlit.io/
- https://github.com/ashrithagoramane/DAMG7245-Spring24/tree/main/repository_structure

## Learning Outcome

1. Design and implement an end-to-end data processing pipeline using modern orchestration tools.
2. Develop robust APIs for data manipulation and retrieval with FastAPI.
3. Manage and process data in cloud-based storage and database solutions.
4. Containerize applications and services for better scalability and deployment.
5. Integrate a front-end web application with backend services for a complete user experience.
6. Apply best practices for version control and documentation for project management.
7. Gain insights into system architecture design following industry standards.
   
## Team Information and Contribution

WE ATTEST THAT WE HAVEN'T USED ANY OTHER STUDENT'S WORK IN OUR ASSIGNMENT AND ABIDE BY THE POLICIES LISTED IN THE STUDENT HANDBOOK

| Name               | Contribution %   | Contributions                                             |
|--------------------|------------------|-----------------------------------------------------------|
| Osborne Lopes      | 40%              | FastAPI, Airflow (30%)                                    |
| Akshita Pathania   | 33.3%            | Streamlit (30%), Documentation, Architecture Diagram      |
| Smithi Parthiban   | 33.3%            | Snowflake Scripts, Streamlit (70%)                        |
| Manimanya Reddy    | 33.3%            | Airflow (70%)                                             |
 

**ARCHITECTURE DIAGRAM**

<img width="1067" alt="Screenshot 2024-03-29 at 8 55 19 AM" src="https://github.com/BigDataIA-Spring2024-Sec1-Team6/Assignment4/assets/114605149/123fe4a7-2362-4b53-b0f5-fe1e1bd89863">



Links: 

CodeLabs Link :- [https://codelabs-preview.appspot.com/?file_id=1ulPzcwcL_LYFQzAODiAhVDi4RdKQZm9SB5UvH9AbDUE#3](https://codelabs-preview.appspot.com/?file_id=1-X2K0jJhhm2IsSHTfBpN8jHKY-AB4Yj-g5DAJMQSAD0#0)

Architectural Diagram - [https://colab.research.google.com/drive/1CTw6ppHcMIPszK8kBkhjIZaAFtuFoN21?usp=sharing](https://colab.research.google.com/drive/1ARtiMF3h7JqUg7ISwqGJ2cuTfiLJRAVe?usp=sharing)
