import requests
import json

url = "https://www.cse.lk/api/todaySharePrice?page=0&size=500"

headers = {
    "User-Agent": "Mozilla/5.0"
}

print("===================================")
print("CSE API TEST")
print("===================================")

response = requests.post(url, headers=headers)

print("Status :", response.status_code)

if response.status_code != 200:
    print(response.text)
    exit()

try:
    data = response.json()
except Exception as e:
    print("JSON Error :", e)
    print(response.text[:1000])
    exit()

print("\nResponse Type :", type(data))

if isinstance(data, list):
    print("Records :", len(data))

    if len(data) > 0:
        print("\nFirst Record:")
        print(json.dumps(data[0], indent=4))

elif isinstance(data, dict):

    print("\nKeys:")
    print(list(data.keys()))

    if "content" in data:
        print("\nContent Records :", len(data["content"]))

        if len(data["content"]) > 0:
            print("\nFirst Record:")
            print(json.dumps(data["content"][0], indent=4))
else:
    print(data)

print("===================================")
print("Finished")
print("===================================")
