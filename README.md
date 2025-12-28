# Compliance Search API

## Description
API to search, normalize, and store compliance-related results in PostgreSQL.

## Setup
1. Python 3.12
2. Create virtual environment:
python -m venv .venv
source .venv/bin/activate # macOS/Linux

4. Install dependencies:


pip install -r requirements.txt


## Run


uvicorn app.main:app --reload

Open http://127.0.0.1:8000/docs to see API documentation.
