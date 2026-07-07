from pydantic import BaseModel, Field
from typing import Optional

class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    body: str = Field(min_length=5, max_length=300)


class NoteUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=1, max_length=100)
    body: object = Field(default=None, min_length=5, max_length=300)


class NoteResponse(BaseModel):
    title: str
    body: str
