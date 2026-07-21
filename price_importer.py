import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}


def test_today_share_price():

    print("========== TODAY SHARE PRICE ==========")

    url = "https://www.cse.lk/api/todaySharePrice"

    try:

        response = requests.post(
            url,
            headers=HEADERS,
            timeout=30
        )

        print("Status :", response.status_code)
        print("Content-Type :", response.headers.get("Content-Type"))

        print("Response :")
        print(response.text[:1000])

    except Exception as e:
        print(e)

    print("========== END ==========")
