import requests
import json

symbol = "JKH.N0000"

url = "https://www.cse.lk/api/companyInfoSummery"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

payload = {
    "symbol": symbol
}


response = requests.post(
    url,
    headers=headers,
    data={
        "symbol": "JKH.N0000"
    }
)
print("Status :", response.status_code)
print("=" * 80)

try:
    data = response.json()
    print(json.dumps(data, indent=2))
except Exception:
    print(response.text)
