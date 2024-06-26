from typing import List

from pydantic import BaseModel


class TextDataInputSchema(BaseModel):
    text: str


class TokenizeOutputSchema(BaseModel):
    result: List[str]


class TaggingOutputSchema(BaseModel):
    result: List[List[str]]


class EntitySchema(BaseModel):
    entity: str
    type: str


class EntitiesRecognizeOutputSchema(BaseModel):
    entities: List[EntitySchema]
