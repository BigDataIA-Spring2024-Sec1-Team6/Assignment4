import requests
import boto3
import xml.etree.ElementTree as ET

def grobid_extraction_file(pdf_file_path, bucket_name, access_key_id, secret_access_key, buffer_size=8192):
    # Define the URL of the GROBID server
    grobid_url = "http://localhost:8070/api/processFulltextDocument"
    
    # Create an S3 client
    s3 = boto3.client(
        's3',
        aws_access_key_id='AKIA47CRX2W7VCWLPNMA',
        aws_secret_access_key='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'
    )
    
    # Download the PDF file from S3
    with open(pdf_file_path, "wb") as file:
        s3.download_fileobj(bucket_name, pdf_file_path, file)
    
    # Send POST request to GROBID API with a buffer
    with open(pdf_file_path, "rb") as file:
        # Create a buffer to read the file in chunks
        buffer = bytearray(buffer_size)
        
        # Initialize the PDF content
        pdf_content = b""
        
        # Read the file in chunks and append to pdf_content
        while True:
            # Read a chunk of data from the file into the buffer
            num_bytes_read = file.readinto(buffer)
            
            # If no more data is read, break out of the loop
            if num_bytes_read == 0:
                break
            
            # Append the chunk to pdf_content
            pdf_content += buffer[:num_bytes_read]
    
    # Send POST request to GROBID API
    response = requests.post(grobid_url, data=pdf_content)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Write the response content to an XML file
        with open('Grobid_Output.xml', 'w', encoding='utf-8') as xml_file:
            xml_file.write(response.text)
        
        # Parse the XML file
        tree = ET.parse('Grobid_Output.xml')
        root = tree.getroot()
        
        # Open a text file for writing the extracted content
        with open('Grobid_Output.txt', 'w', encoding='utf-8') as text_file:
            for elem in root.iter():
                if elem.text:
                    text_file.write(elem.text + '\n')  # Write text content followed by a newline
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    # Specify the path to the PDF file you want to process in the S3 bucket
    pdf_file_path = "s3://airflowassign/2024-l1-topics-combined-2.pdf"
    
    # Specify your S3 bucket name
    bucket_name = "airflowassign"
    
    # Specify your AWS access key ID and secret access key
    access_key_id = "AKIA47CRX2W7VCWLPNMA"
    secret_access_key = "nD8ruZVqdXQ6sZNv8gU4A/n+EOxdTE8CSRdwHVLR"
    
    # Call the function to extract data using GROBID
    grobid_extraction_file(pdf_file_path, bucket_name, access_key_id, secret_access_key)
