import os
import requests

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}


def insert_daily_price(data):
    url = SUPABASE_URL + "/rest/v1/daily_prices"

    response = requests.post(
        url,
        headers=HEADERS,
        json=data,
        timeout=30
    )

    print("Insert Status :", response.status_code)

    if response.text:
        print(response.text)

    return response.status_code
