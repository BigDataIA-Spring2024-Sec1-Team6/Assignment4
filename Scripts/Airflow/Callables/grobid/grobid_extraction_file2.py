#pip install requests

def grobid_extraction_file2():
    import requests
# Define the URL of the GROBID server
grobid_url = "http://localhost:8070/api/processFulltextDocument"

#For the First PDF:
# Define the path to the PDF file you want to process
pdf_file_path = "/Users/akshitapathania/Downloads/Archive_2/2024-l3-topics-combined-2.pdf"

# Read the PDF file as binary
with open(pdf_file_path, "rb") as file:
    pdf_content = file.read()    
    
# Define request headers
headers = {"Content-Type": "application/pdf"}

response=requests.post(grobid_url, files={'input': open(pdf_file_path, 'rb')})

# Send POST request to GROBID API
#response = requests.post(grobid_url, data=pdf_content, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Print the response content (extracted structured data)
    print(response.text)
else:
    print("Error:", response.text)

# Assuming 'response' is the variable containing the response object from a request
response_text = response.text

# Open a file in write mode. The 'with' statement ensures the file is properly closed after writing.
# Here, 'response_data.xml' is the name of the file. Change the extension to '.txt' if preferred.
# 'encoding='utf-8'' ensures that the file is saved with UTF-8 encoding, which is a good practice for text data.
with open('/Users/akshitapathania/Desktop/Grobid_RR_2024_l3_combined_2.xml', 'w', encoding='utf-8') as file:
    file.write(response_text)


import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse('/Users/akshitapathania/Desktop/Grobid_RR_2024_l3_combined_2.xml')
root = tree.getroot()

# Open a text file for writing the extracted content
with open('Grobid_RR_l3_combined_2.txt', 'w', encoding='utf-8') as text_file:
    for elem in root.iter():
        if elem.text:
            text_file.write(elem.text + '\n')  # Write text content followed by a newline
