import requests

URLS = [
    "https://www.cse.lk/api/todaySharePrice",
    "https://www.cse.lk/api/marketSummary",
    "https://www.cse.lk/api/companyInfoSummery",
    "https://www.cse.lk/api/companyList",
    "https://www.cse.lk/api/listedCompanies",
    "https://www.cse.lk/api/tradeSummary",
    "https://www.cse.lk/api/stockPrice",
    "https://www.cse.lk/api/security",
]

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

print("=" * 60)
print("CSE API SCANNER")
print("=" * 60)

for url in URLS:

    print("\nURL :", url)

    # GET
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)

        print("GET :", r.status_code)

        text = r.text.replace("\n", " ")

        print(text[:250])

    except Exception as e:
        print("GET ERROR :", e)

    # POST
    try:
        r = requests.post(url, headers=HEADERS, timeout=20)

        print("POST :", r.status_code)

        text = r.text.replace("\n", " ")

        print(text[:250])

    except Exception as e:
        print("POST ERROR :", e)

print("\nFinished.")
