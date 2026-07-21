import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def scan_homepage():
    print("========== CSE Scanner ==========")

    url = "https://www.cse.lk/"

    try:
        response = requests.get(url, headers=HEADERS, timeout=30)

        print("CSE Home Status :", response.status_code)
        print("Content-Type :", response.headers.get("Content-Type"))

        soup = BeautifulSoup(response.text, "lxml")

        if soup.title:
            print("Page Title :", soup.title.text.strip())

        print("\nFirst 20 Links")

        links = soup.find_all("a", href=True)

        count = 0

        for link in links:
            href = link.get("href")

            if href:
                print(href)
                count += 1

            if count >= 20:
                break

        print("Total Links Found :", len(links))

    except Exception as e:
        print("Scanner Error :", e)

    print("========== Scan Finished ==========")


def test_market_summary():
    print("\n========== Market Summary API ==========")

    url = "https://www.cse.lk/api/marketSummery"

    try:
        response = requests.post(
            url,
            headers=HEADERS,
            timeout=30
        )

        print("Status :", response.status_code)
        print("Content-Type :", response.headers.get("Content-Type"))
        print("Response :")
        print(response.text[:500])

    except Exception as e:
        print("API Error :", e)

    print("========== API Test Finished ==========")
