import os
from pprint import pprint

from dotenv import load_dotenv
from pandas import read_csv
from plotly.express import line

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}&datatype=csv"

df = read_csv(request_url)

import os
from pprint import pprint

from dotenv import load_dotenv
from pandas import read_csv
from plotly.express import line

load_dotenv()

API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")

request_url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={API_KEY}&datatype=csv"

df = read_csv(request_url)

# Challenge A
# What is the most recent unemployment rate? And the corresponding date? Display the unemployment rate using a percent sign.

print("-------------------------")
print("LATEST UNEMPLOYMENT RATE:")
first_row = df.iloc[0]
print(f"{first_row['value']}%", "as of", first_row["timestamp"])