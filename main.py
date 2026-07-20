import requests
import json
from datetime import datetime

print("===================================")
print("CSE AI Auto Sync Started")
print("Time :", datetime.now())
print("===================================")

SUPABASE_URL = "YOUR_SUPABASE_URL"
SUPABASE_KEY = "YOUR_SUPABASE_API_KEY"

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}
