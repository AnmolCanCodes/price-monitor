import requests
from bs4 import BeautifulSoup

def scrape_product(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    price_text = soup.find("h4", class_="price").text.strip()
    price = float(price_text.replace("$", "").replace(",", ""))

    stock_text = soup.find("p", class_="in-stock")
    in_stock = True
    if stock_text is not None:
        in_stock = "in stock" in stock_text.text.strip().lower()

    return {
        "price": price,
        "in_stock": in_stock
    }
