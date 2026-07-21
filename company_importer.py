import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

CANDIDATE_ENDPOINTS = [
    "https://www.cse.lk/api/companyInfoSummery",
    "https://www.cse.lk/api/companyList",
    "https://www.cse.lk/api/listedCompanies",
    "https://www.cse.lk/api/companies"
]


def test_company_api():
    print("========== COMPANY API TEST ==========")

    for url in CANDIDATE_ENDPOINTS:
        print(f"\nTesting: {url}")

        try:
            response = requests.post(
                url,
                headers=HEADERS,
                timeout=30
            )

            print("Status:", response.status_code)
            print("Content-Type:", response.headers.get("Content-Type"))
            print(response.text[:400])

        except Exception as e:
            print("ERROR:", e)

    print("\n========== END ==========")
