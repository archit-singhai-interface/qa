from pydantic import BaseModel
from typing import List


class Question(BaseModel):
    text: str


class Answer(BaseModel):
    text: str
    sources: List[str]
    content: List[str]
