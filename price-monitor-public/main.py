import pandas as pd
from datetime import datetime
from scraper import scrape_product
import os

products = pd.read_csv("/home/anmol/Desktop/Automation/price_monitor/products.csv")

history_file = "/home/anmol/Desktop/Automation/price_monitor/price_history.csv"

if os.path.exists(history_file):
    history = pd.read_csv(history_file)
else:
    history = pd.DataFrame(columns=["timestamp","product","price","in_stock"])

alerts = []

for _, row in products.iterrows():
    name = row["product_name"]
    url = row["url"]
    threshold = row["threshold_percent"]

    data = scrape_product(url)

    new_price = data["price"]
    in_stock = data["in_stock"]

    product_history = history[history["product"] == name]

    if not product_history.empty:
        old_price = product_history.iloc[-1]["price"]
        percent_change = ((new_price - old_price) / old_price) * 100

        if percent_change <= -threshold:
            alerts.append(
                f"<b>{name}</b> price dropped {abs(percent_change):.2f}%<br>"
                f"Old: ${old_price} → New: ${new_price}<br><br>"
            )
        if percent_change >= threshold:
            alerts.append(
                f"<b>{name}</b> price increased {percent_change:.2f}%<br>"
                f"Old: ${old_price} → New: ${new_price}<br><br>"
            )
        else:
            print(f"{name} price change is within threshold: {percent_change:.2f}%")
        

    if not in_stock:
        alerts.append(f"<b>{name}</b> is OUT OF STOCK!<br><br>")

    history.loc[len(history)] = [
        datetime.now().isoformat(),
        name,
        new_price,
        in_stock
    ]

history.to_csv(history_file, index=False)

print("Price history updated.")


import os
from dotenv import load_dotenv

load_dotenv()  

SENDER = os.getenv("EMAIL_SENDER")
PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER = os.getenv("EMAIL_RECEIVER")

if alerts:
    from alert import send_email

    if not all([SENDER, PASSWORD, RECEIVER]):
        print("⚠️  Missing email configuration. Please set EMAIL_SENDER,"
              " EMAIL_PASSWORD and EMAIL_RECEIVER in your environment.")
    else:
        try:
            send_email("".join(alerts), SENDER, PASSWORD, RECEIVER)
            print("Alerts sent.")
        except Exception as exc:
            print(f"Failed to send alerts: {exc}")
else:
    
    print("No alerts generated; nothing to email.")
