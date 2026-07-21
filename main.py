import os
from datetime import datetime
import requests

from cse_scraper import scan_homepage, test_market_summary

print("===================================")
print("CSE AI Auto Sync Started")
print("Time :", datetime.now())
print("===================================")

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}


def test_supabase():
    url = SUPABASE_URL + "/rest/v1/stocks?select=*"

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=30
    )

    print("Supabase Status :", response.status_code)

    if response.status_code == 200:
        print("Supabase Connected")
    else:
        print("Supabase Error")
        print(response.text)


def test_cse():
    url = "https://www.cse.lk/"

    response = requests.get(
        url,
        timeout=30
    )

    print("CSE Status :", response.status_code)

    if response.status_code == 200:
        print("CSE Website Connected")
    else:
        print("Cannot connect to CSE")


def main():
    print("===================================")
    print("Starting Tests")
    print("===================================")

    test_supabase()
    test_cse()

    print("===================================")
    print("Starting CSE Scanner")
    print("===================================")

    scan_homepage()

    print("===================================")
    print("Testing Market Summary API")
    print("===================================")

    test_market_summary()

    print("===================================")
    print("All Tests Finished")
    print("===================================")


if __name__ == "__main__":
    main()
