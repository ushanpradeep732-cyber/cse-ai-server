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

# -----------------------------
# Load Stocks
# -----------------------------
stocks_url = SUPABASE_URL + "/rest/v1/stocks?select=id,symbol"

response = requests.get(stocks_url, headers=HEADERS)

if response.status_code != 200:
    print("Cannot load stocks")
    print(response.text)
    raise SystemExit()

stocks = response.json()

stock_map = {}

for s in stocks:
    stock_map[s["symbol"]] = s["id"]

print("Stocks Loaded :", len(stock_map))

# -----------------------------
# Download Today Prices
# -----------------------------
url = "https://www.cse.lk/api/todaySharePrice?page=0&size=300"

response = requests.post(
    url,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)

print("CSE Status :", response.status_code)

if response.status_code != 200:
    print(response.text)
    raise SystemExit()

data = response.json()

if isinstance(data, dict):
    prices = data.get("content", [])
else:
    prices = data

print("Price Records :", len(prices))

today = datetime.now().strftime("%Y-%m-%d")

count = 0
skip = 0
failed = 0

symbols = sorted(stock_map.keys())

print("Companies :", len(symbols))

for symbol in symbols:

    print("Processing :", symbol)

    response = requests.post(
        f"https://www.cse.lk/api/companyInfoSummery?symbol={symbol}",
        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "application/json"
        }
    )

    if response.status_code != 200:
        print("API Error :", symbol, response.status_code)
        failed += 1
        continue

    try:
        data = response.json()
        info = data.get("reqSymbolInfo")

        if info is None:
            failed += 1
            continue

    except Exception as e:
        print("JSON Error :", symbol, str(e))
        failed += 1
        continue

    payload = {
        "stock_id": stock_map[symbol],
        "trade_date": today,
        "open_price": info.get("previousClose"),
        "high_price": info.get("hiTrade"),
        "low_price": info.get("lowTrade"),
        "close_price": info.get("lastTradedPrice"),
        "volume": info.get("tdyShareVolume", 0)
    }

    r = requests.post(
    SUPABASE_URL + "/rest/v1/daily_prices?on_conflict=stock_id,trade_date",
    headers={
        **HEADERS,
        "Prefer": "resolution=merge-duplicates"
    },
    json=payload
)

if r.status_code in (200, 201):
    count += 1

elif r.status_code == 409:
    skip += 1

else:
    print("-----------------------------------")
    print("Insert Error :", symbol)
    print("Status :", r.status_code)
    print(r.text)
    failed += 1

print("===================================")
print("Imported :", count)
print("Skipped :", skip)
print("Failed :", failed)
print("Finished")
print("===================================")
