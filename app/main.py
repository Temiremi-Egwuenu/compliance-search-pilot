from fastapi import FastAPI

app = FastAPI(title="Compliance Search Pilot")

@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "Compliance Search Pilot is running"
    }
@app.get("/search")
def search(q: str):
    return {"query": q}
