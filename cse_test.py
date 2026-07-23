import requests

symbols = [
    "JKH.N0000",
    "COMB.N0000",
    "HNB.N0000",
    "LOLC.N0000",
    "SAMP.N0000"
]

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

for symbol in symbols:

    url = f"https://www.cse.lk/api/companyInfoSummery?symbol={symbol}"

    response = requests.post(url, headers=headers)

    print("=" * 70)
    print(symbol)
    print("Status :", response.status_code)

    if response.status_code != 200:
        print(response.text)
        continue

    data = response.json()

    info = data.get("reqSymbolInfo")

    if info is None:
        print("No Symbol Info")
        continue

    print("Price :", info.get("lastTradedPrice"))
    print("Previous :", info.get("previousClose"))
    print("High :", info.get("hiTrade"))
    print("Low :", info.get("lowTrade"))
    print("Volume :", info.get("tdyShareVolume"))
