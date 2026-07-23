import requests

url = "https://www.cse.lk/api/companyInfoSummery"

response = requests.post(
    url,
    params={
        "symbol": "JKH.N0000"
    },
    headers={
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }
)

print("Status :", response.status_code)
print(response.text)
