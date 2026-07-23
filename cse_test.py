import requests
import json

url = "https://www.cse.lk/api/todaySharePrice?page=0&size=300"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.post(url, headers=headers)

print("Status:", response.status_code)
print("=" * 80)

data = response.json()

if isinstance(data, dict):
    print("TYPE : DICT")
    print("KEYS :", list(data.keys()))

    print("\nFULL RESPONSE:\n")
    print(json.dumps(data, indent=2))

else:
    print("TYPE : LIST")
    print("RECORDS :", len(data))

    print("\nFIRST RECORD\n")
    print(json.dumps(data[0], indent=2))
