from app.stocks import format_usd, fetch_stocks_data
from pandas import DataFrame

def test_usd_formatting():
    assert format_usd(4.5) == "$4.50"
    assert format_usd(4.555555555555) == "$4.56"
    assert format_usd(1000000) == "$1,000,000.00"

def test_data_fetching():
    result = fetch_stocks_data("NFLX")
    assert isinstance(result, DataFrame)
    
    assert "timestamp" in result.columns
    assert "adjusted_close" in result.columns
    assert "high" in result.columns
    assert "low" in result.columns

    assert len(result) >= 100