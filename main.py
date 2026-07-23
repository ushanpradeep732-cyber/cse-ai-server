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

pri
