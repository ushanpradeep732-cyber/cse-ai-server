import requests

URLS = [
    "https://www.cse.lk/",
    "https://www.cse.lk/pages/market-summary/market-summary.component.html",
    "https://www.cse.lk/api"
]

def scan_homepage():
    print("========== CSE Scanner ==========")

    for url in URLS:
        print(f"\nTesting : {url}")

        try:
            response = requests.get(url, timeout=30)

            print("Status :", response.status_code)
            print("Content-Type :", response.headers.get("Content-Type"))

            print("First 300 Characters")
            print(response.text[:300])

        except Exception as e:
            print("ERROR :", e)

    print("\n========== Scan Finished ==========")
