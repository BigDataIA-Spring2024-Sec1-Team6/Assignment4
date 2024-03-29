def metadata_class_file():
from pydantic import BaseModel, ValidationError, constr, conint, validator
from datetime import datetime
from pathlib import Path

class MetaDataPDFClass(BaseModel):
    file_path: constr(min_length=1, max_length=200)
    file_size: constr(min_length=1, max_length=200)
    number_of_articles: conint(gt=0)  # Positive integer, required
    creation_time: datetime
    modification_time: datetime
    encoding_language: constr(min_length=1, max_length=200)

    @validator('file_path')
    @classmethod
    def validate_file_path(cls, value):
        file_path = Path(value)
        if not file_path.exists():  # Check if file_path exists
            raise ValueError('File path does not exist')
        return value

    @validator('file_size')
    @classmethod
    def validate_file_size(cls, value):
        if not re.match(r'^\d+(?:\.\d+)?\s?(KB|MB|GB)$', value):
            raise ValueError('file_size must be a numeric value followed by KB, MB, or GB')
        return value
    
    @validator('number_of_articles')
    @classmethod
    def validate_number_of_articles(cls, value):
        # No need for strip() as it's an integer
        # Custom validation logic for number_of_articles, if needed
        return value

    @validator('creation_time', 'modification_time', pre=True)
    @classmethod
    def validate_datetime(cls, value):
        if not isinstance(value, datetime):
            raise ValueError('Invalid datetime format')
        return value

    @validator('encoding_language')
    @classmethod
    def validate_encoding_language(cls, value):
        known_encodings = ['UTF-8', 'ASCII', 'ISO-8859-1']  # Extend this list as needed
        if value not in known_encodings:
            raise ValueError('encoding_language must be a known encoding type')
        return value

