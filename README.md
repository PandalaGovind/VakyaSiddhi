# VakyaSiddhi (वाक्यसिद्धि)

An intelligent, full-stack text editing assistant powered by Python, FastAPI, and React. VakyaSiddhi analyzes input text and provides word corrections using candidate generation and language modeling techniques.

## Project Structure
- `backend/`: FastAPI application, NLP processing, and candidate generation engine.
- `frontend/`: React application (powered by Vite) providing an editor UI.

## Getting Started

### 1. Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload