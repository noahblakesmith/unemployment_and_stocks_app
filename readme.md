# My Unemployment Report


## Setup


Create and activate a virtual environment:

```sh
conda create -n unemployment-env python=3.8

conda activate unemployment-env

Navigate to directory where files are located.
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Configuration


[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Then create a local ".env" file and provide the key like this:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY = "_________"
```


## Usage

Run the unemployment report:

```sh
python unemployment_solution_json.py

python unemployment_solution_csv.py

# or pass env var from command line:

ALPHAVANTAGE_API_KEY = "______" python unemployment_solution_json.py

ALPHAVANTAGE_API_KEY = "______" python unemployment_solution_csv.py
```