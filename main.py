import os
import requests
from datetime import datetime

SUPABASE_URL = os.environ["SUPABASE_URL"]
SUPABASE_KEY = os.environ["SUPABASE_KEY"]

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

print("===================================")
print("CSE AI AUTO IMPORT")
print(datetime.now())
print("===================================")

# --------------------------
# Load Stocks from Supabase
# --------------------------

stocks_url = SUPABASE_URL + "/rest/v1/stocks?select=id,symbol"

stocks = requests.get(stocks_url, headers=HEADERS).json()

stock_map = {}

for s in stocks:
    stock_map[s["symbol"]] = s["id"]

print("Stocks Loaded :", len(stock_map))

# --------------------------
# Download CSE Prices
# --------------------------

url = "https://www.cse.lk/api/todaySharePrice"

response = requests.get(url)

print("CSE Status :", response.status_code)

prices = response.json()

today = datetime.now().strftime("%Y-%m-%d")

count = 0

for item in prices:

    symbol = item["symbol"]

    if symbol not in stock_map:
        continue

    payload = {
        "stock_id": stock_map[symbol],
        "trade_date": today,
        "open_price": item.get("open"),
        "high_price": item.get("high"),
        "low_price": item.get("low"),
        "close_price": item.get("lastTradedPrice"),
        "volume": item.get("quantity", 0)
    }

    requests.post(
        SUPABASE_URL + "/rest/v1/daily_prices",
        headers={
            **HEADERS,
            "Prefer": "resolution=merge-duplicates"
        },
        json=payload
    )

    count += 1

print("===================================")
print("Imported :", count)
print("Finished")
print("===================================")
