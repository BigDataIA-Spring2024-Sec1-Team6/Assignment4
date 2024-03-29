def content_extraction_file():
    import xml.etree.ElementTree as ET
    import pandas as pd
    import csv
    import re
    import numpy as np


def parse_my_files(file_path, title, level):
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Namespace handling
    ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

    df = pd.DataFrame(columns=['level', 'title', 'topic', 'learning_outcomes', 'file_path'])

    # Iterate through each 'div' element in the XML
    for div in root.findall('.//tei:div', ns):
        topic = div.find('./tei:head', ns).text if div.find('./tei:head', ns) is not None else ''
        learning_outcomes = " ".join([p.text for p in div.findall('./tei:p/tei:s', ns) if p.text])

        if learning_outcomes:
            df = df.append({
                'level': level,
                'title': title,
                'topic': topic,
                'learning_outcomes': learning_outcomes,
                'file_path': file_path
            }, ignore_index=True)

    return df


list_df = []
for x in range(1, 4):
    if x == 1:
        Level = "Level I"
        new_df = parse_my_files(file_path=f"/content/GROBID-2024-l{x}-topics-combined-2.xml", title="Derivatives", level=Level)
    elif x == 2:
        Level = "Level II"
        new_df = parse_my_files(file_path=f"/content/GROBID-2024-l{x}-topics-combined-2.xml", title="Quantitative Methods", level=Level)
    elif x == 3:
        Level = "Level III"
        new_df = parse_my_files(file_path=f"/content/GROBID-2024-l{x}-topics-combined-2.xml", title="Economics", level=Level)

    list_df.append(new_df)


final_df = pd.concat(list_df, ignore_index=True)
final_df = final_df.fillna(np.nan).replace([np.nan], [None])
final_df['learning_outcomes'] = final_df['learning_outcomes'].apply(lambda v: re.sub(r'[\'"‘’”“]|<.*?>', '', str(v)))

validate_record_count = 0
contentinstance_list = []

for i, row in final_df.iterrows():
    try:
        obj = ContentClass(level=row.level, title=row.title, topic=row.topic, learning_outcomes=row.learning_outcomes, file_path=row.file_path)
        contentinstance_list.append(obj)
        validate_record_count += 1
    except Exception as ex:
        print(ex)

def write_to_csv(obj_list):
    fieldnames = list(ContentClass.schema()["properties"].keys())

    with open("/content/content_data2.csv", "w", encoding='utf-8', newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames, quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for obj in obj_list:
            writer.writerow(obj.model_dump())

if validate_record_count == final_df.shape[0]:
    print("Successfully validated")
    write_to_csv(contentinstance_list)
else:
    print("Validation failed in some records. Please fix and retry")