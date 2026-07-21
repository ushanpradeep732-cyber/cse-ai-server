import os
from datetime import datetime
import requests

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

    response = requests.get(url, headers=HEADERS)

    print("Supabase Status :", response.status_code)

    if response.status_code == 200:
        print("Supabase Connected")
    else:
        print(response.text)

def test_cse():
    url = "https://www.cse.lk/"

    response = requests.get(url, timeout=30)

    print("CSE Status :", response.status_code)

    if response.status_code == 200:
        print("CSE Website Connected")
    else:
        print("Cannot connect to CSE")

if __name__ == "__main__":
    test_supabase()
    test_cse()
