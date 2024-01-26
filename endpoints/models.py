from typing import List
from pydantic import BaseModel

class FrCard(BaseModel):
    cardid: str
    card: str

class FrWord(BaseModel):
    wordid: str
    word: str

class EnCard(BaseModel):
    cardid: str
    card: str

class EnWord(BaseModel):
    wordid: str
    word: str

class WordHistory(BaseModel):
    history: List[str]

class CardHistory(BaseModel):
    history: List[str]

class SemanticSearchTerms(BaseModel):
    search_term: str
    category: str | None = None
    region: str | None = None
