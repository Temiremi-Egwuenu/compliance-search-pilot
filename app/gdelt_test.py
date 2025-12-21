import requests

url = "https://api.gdeltproject.org/api/v2/doc/doc"

params = {
    "query": "compliance",
    "mode": "artlist",
    "format": "json",
    "maxrecords": 5
}

response = requests.get(url, params=params)

print("Status Code:", response.status_code)
print(response.json())