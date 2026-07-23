import requests
import json

url = "https://www.cse.lk/api/todaySharePrice"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

payload = {
    "page": 0,
    "size": 300
}

response = requests.post(url, headers=headers, json=payload)

print("Status :", response.status_code)

try:
    data = response.json()

    if isinstance(data, list):
        print("Records :", len(data))
        print(json.dumps(data[:3], indent=2))
    else:
        print(json.dumps(data, indent=2))

except Exception:
    print(response.text)
