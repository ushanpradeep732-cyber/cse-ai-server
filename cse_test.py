import requests
import json

url = "https://www.cse.lk/api/allSecurityCode"

response = requests.post(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("Status :", response.status_code)

if response.status_code == 200:
    data = response.json()

    print("Records :", len(data))
    print()

    print(json.dumps(data[:5], indent=2))
else:
    print(response.text)
