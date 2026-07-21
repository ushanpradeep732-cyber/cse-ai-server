import requests

headers = {
    "User-Agent": "Mozilla/5.0"
}

urls = [
    "https://www.cse.lk/api/todaySharePrice",
    "https://www.cse.lk/api/marketSummary"
]

for url in urls:

    print("=" * 60)
    print(url)

    try:
        r = requests.get(url, headers=headers)
        print("GET :", r.status_code)
        print(r.text[:300])
    except Exception as e:
        print(e)

    print("-" * 40)

    try:
        r = requests.post(url, headers=headers)
        print("POST :", r.status_code)
        print(r.text[:300])
    except Exception as e:
        print(e)
