import os
import time
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

stocks_url = SUPABASE_URL + "/rest/v1/stocks?select=id,symbol"

response = requests.get(
    stocks_url,
    headers=HEADERS
)

if response.status_code != 200:
    print("Cannot load stocks")
    print(response.text)
    exit()

stocks = response.json()

stock_map = {}

for row in stocks:
    stock_map[row["symbol"]] = row["id"]

symbols = list(stock_map.keys())

today = datetime.now().strftime("%Y-%m-%d")

imported = 0
skipped = 0
failed = 0

total = len(symbols)

print("Stocks Loaded :", total)

print("===================================")

for index, symbol in enumerate(symbols, start=1):

    print(f"[{index}/{total}] {symbol}")

    url = (
        "https://www.cse.lk/api/companyInfoSummery"
        f"?symbol={symbol}"
    )

    try:

        response = requests.post(
            url,
            headers={
                "User-Agent": "Mozilla/5.0",
                "Accept": "application/json"
            },
            timeout=30
        )

        if response.status_code != 200:
            print("HTTP Error :", response.status_code)
            failed += 1
            continue

        data = response.json()

        info = data.get("reqSymbolInfo")

        if info is None:
            print("No data")
            skipped += 1
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

        r = requ
