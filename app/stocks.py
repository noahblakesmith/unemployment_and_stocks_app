def format_usd(my_price):
    return f"${my_price:,.2f}"

if __name__ == "__main__":

    from pandas import read_csv
    from app.alpha import API_KEY

    print("STOCKS REPORT...")

    symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"
    print("SYMBOL:", symbol)

    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={API_KEY}&datatype=csv"

    df = read_csv(request_url)
    print(df.columns)
    print(df.head())

    latest = df.iloc[0]

    print("LATEST:", format_usd(latest["adjusted_close"]), "as of", latest["timestamp"])
    print("HIGH:", format_usd(df["high"].max()))
    print("LOW:", format_usd(df["low"].min()))