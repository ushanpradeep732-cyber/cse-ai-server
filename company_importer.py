import requests
import json

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Content-Type": "application/json"
}


def test_company_api():

    symbol = "JKH.N0000"

    url = "https://www.cse.lk/api/companyInfoSummery"

    payload = {
        "symbol": symbol
    }

    print("===================================")
    print("COMPANY INFO TEST")
    print("===================================")
    print("Symbol :", symbol)

    try:

        response = requests.post(
            url,
            headers=HEADERS,
            json=payload,
            timeout=30
        )

        print("Status :", response.status_code)
        print("Content-Type :", response.headers.get("Content-Type"))

        print("Response:")
        print(response.text)

        if response.status_code == 200:
            try:
                data = response.json()

                print("\nParsed JSON")
                print(json.dumps(data, indent=2))

            except Exception:
                print("JSON Parse Failed")

    except Exception as e:
        print("ERROR :", e)

    print("===================================")
    print("TEST FINISHED")
    print("===================================")
