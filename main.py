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

# ---------------------------------
# Load Stocks from Supabase
# ---------------------------------

stocks_url = SUPABASE_URL + "/rest/v1/stocks?select=id,symbol"

response = requests.get(stocks_url, headers=HEADERS)

if response.status_code != 200:
    print("Cannot load stocks.")
    print(response.text)
    exit()

stocks = response.json()

stock_map = {}

for s in stocks:
    stock_map[s["symbol"]] = s["id"]

print("Stocks Loaded :", len(stock_map))

# ---------------------------------
# Download Today Share Prices
# ---------------------------------

url = "https://www.cse.lk/api/todaySharePrice"

response = response = requests.post(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("CSE Status :", response.status_code)

if response.status_code != 200:
    print(response.text)
    exit()

data = response.json()

# API may return either a list or {"content":[...]}
if isinstance(data, dict):
    prices = data.get("content", [])
else:
    prices = data

print("Price Records :", len(prices))

today = datetime.now().strftime("%Y-%m-%d")

count = 0

for item in prices:

    if not isinstance(item, dict):
        continue

    symbol = item.get("symbol")

    if not symbol:
        continue

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

    r = requests.post(
        SUPABASE_URL + "/rest/v1/daily_prices",
        headers={
            **HEADERS,
            "Prefer": "resolution=merge-duplicates"
        },
        json=payload
    )

    if r.status_code not in (200, 201):
        print("Insert Error :", symbol)
        print("Status :", r.status_code)
        print(r.text)
    else:
        count += 1

print("===================================")
print("Imported :", count)
print("Finished")
print("===================================")
