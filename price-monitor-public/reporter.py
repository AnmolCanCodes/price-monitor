import pandas as pd

def generate_report():
    history = pd.read_csv("price_history.csv")
    latest = history.sort_values("timestamp").groupby("product").tail(1)
    latest.to_excel("report.xlsx", index=False)


if __name__ == "__main__":
    try:
        generate_report()
        print(f"report written to {'report.xlsx'}")
    except Exception as exc:
        print(f"failed to generate report: {exc}")