import requests
import json
from datetime import datetime

print("===================================")
print("CSE AI Auto Sync Started")
print("Time :", datetime.now())
print("===================================")

import os

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
        headers=HEADERS
    )

    print("Status :", response.status_code)
    print(response.text)


if __name__ == "__main__":
    test_supabase()
