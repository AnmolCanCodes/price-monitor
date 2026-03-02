def generate_report():
    history = pd.read_csv("price_history.csv")
    
    latest = history.sort_values("timestamp").groupby("product").tail(1).reset_index(drop=True)
    
    previous = history.sort_values("timestamp").groupby("product").tail(2).groupby("product").head(1).reset_index(drop=True)
    
    report = latest[["product", "price", "in_stock", "timestamp"]].copy()
    report.rename(columns={"price": "current_price"}, inplace=True)
    
    previous_prices = previous[["product", "price"]].rename(columns={"price": "previous_price"})
    report = report.merge(previous_prices, on="product", how="left")
    
    report["price_change"] = report["current_price"] - report["previous_price"]
    report["percent_change"] = ((report["current_price"] - report["previous_price"]) / report["previous_price"] * 100).round(2)
    
    report = report[["product", "previous_price", "current_price", "price_change", "percent_change", "in_stock", "timestamp"]]
    
    report.to_excel("report.xlsx", index=False)


if __name__ == "__main__":
    try:
        generate_report()
        print(f"report written to {'report.xlsx'}")
    except Exception as exc:
        print(f"failed to generate report: {exc}")
