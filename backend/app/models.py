from pydantic import BaseModel
from typing import List

class CorrectionRequest(BaseModel):
    word: str

class CandidateSuggestion(BaseModel):
    word: str
    score: float

class CorrectionResponse(BaseModel):
    original: str
    suggestions: List[CandidateSuggestion]