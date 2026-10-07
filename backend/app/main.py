import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import CorrectionRequest, CorrectionResponse
from app.engine import AutocorrectEngine

app = FastAPI(
    title="VakyaSiddhi API",
    description="Context-Aware Autocorrect Backend Engine",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CORPUS_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "corpus.txt")
engine = AutocorrectEngine(corpus_path=CORPUS_PATH)

@app.get("/")
def root():
    return {"status": "online", "system": "VakyaSiddhi API"}

@app.post("/api/correct", response_model=CorrectionResponse)
def correct_word(payload: CorrectionRequest):
    suggestions = engine.get_corrections(payload.word)
    return {
        "original": payload.word,
        "suggestions": suggestions
    }