def content_class_file():

    from pydantic import BaseModel, field_validator, ValidationError, ValidationInfo
    import re

class ContentClass(BaseModel):
    level: str
    title: str
    topic: str
    learning_outcomes: str
    file_path: str

    @field_validator('title', 'level', 'learning_outcomes')
    @classmethod
    def text_should_not_contain_html_or_quotes(cls, v: str, info: ValidationInfo) -> str:
        if v and re.search(r'[\'"‘’”“]|<.*?>', v):
            raise ValueError(f'{info.field_name} contains invalid characters like quotes or html tags')
        return v

    @field_validator('level')
    @classmethod
    def level_must_match_pattern(cls, v: str) -> str:
        if not re.search(r"Level\s+(I|II|III)\b", v):
            raise ValueError('level is not valid')
        return v
