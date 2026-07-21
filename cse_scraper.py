import requests
from bs4 import BeautifulSoup

def scan_homepage():
    url = "https://www.cse.lk/"

    response = requests.get(url, timeout=30)

    print("CSE Home Status:", response.status_code)

    if response.status_code != 200:
        return

    soup = BeautifulSoup(response.text, "lxml")

    print("Page Title:")
    print(soup.title.text.strip())

    print("Links Found:")
    links = soup.find_all("a", href=True)

    for link in links[:20]:
        print(link["href"])
