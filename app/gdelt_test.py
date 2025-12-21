import requests


def fetch_gdelt_articles(query, max_records=5):
    url = "https://api.gdeltproject.org/api/v2/doc/doc"
    params = {
        "query": query,
        "mode": "artlist",
        "format": "json",
        "maxrecords": max_records
    }

    response = requests.get(url, params=params)
    data = response.json()

    normalized = []
    for article in data.get("articles", []):
        normalized.append({
            "source": article.get("domain", "unknown"),
            "title": article.get("title", ""),
            "snippet": article.get("title", ""),  # GDELT doesn’t give a snippet, so use title
            "url": article.get("url", "")
        })

    return normalized


# Test
if __name__ == "__main__":
    results = fetch_gdelt_articles("compliance")
    for r in results:
        print(r)
