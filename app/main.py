import sys
import os
sys.path.append(os.path.dirname(__file__))
from db import get_connection

# app/main.py
from fastapi import FastAPI, Query
from db import get_connection

app = FastAPI()

# Example of normalized data structure
def normalize_results(raw_results):
    """
       Converts raw API results into a standard format.

       Args:
           raw_results (list of dict): List of results from API.

       Returns:
           list of dict: Normalized results with keys 'source', 'title', 'snippet', 'url'.
       """
    clean_results = []
    for r in raw_results:
        clean_results.append({
            "source": r.get("source", ""),
            "title": r.get("title", ""),
            "snippet": r.get("snippet", ""),
            "url": r.get("url", "")
        })
    return clean_results

@app.get("/search")
def search(q: str = Query(...)):
    """
       Handles search requests:
       1. Stores the search term in the database.
       2. Fetches results from live API (placeholder for now).
       3. Normalizes results.
       4. Stores results in the database.
       5. Returns JSON response with search term and results.

       Args:
           q (str): Query string.

       Returns:
           dict: Contains query and list of normalized results.
    """
    # --- 1. Connect to DB ---
    conn = get_connection()
    cur = conn.cursor()

    # --- 2. Insert search term ---
    cur.execute("INSERT INTO searches (query) VALUES (%s) RETURNING id", (q,))
    search_id = cur.fetchone()[0]
    conn.commit()

    # --- 3. Call your live API (example placeholder) ---
    raw_results = [
        {"source": "Example Source", "title": f"Result for {q}", "snippet": "Snippet here", "url": "http://example.com"}
    ]

    # --- 4. Normalize results ---
    results = normalize_results(raw_results)

    # --- 5. Insert results into DB ---
    for r in results:
        cur.execute("""
            INSERT INTO results (search_id, source, title, snippet, url)
            VALUES (%s, %s, %s, %s, %s)
        """, (search_id, r['source'], r['title'], r['snippet'], r['url']))
    conn.commit()

    # --- 6. Close DB connection ---
    cur.close()
    conn.close()

    # --- 7. Return results ---
    return {"query": q, "results": results}
