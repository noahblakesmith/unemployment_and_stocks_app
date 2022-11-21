# My Unemployment Report


## Setup


Create and activate a virtual environment:

```sh
conda create -n unemployment-env python=3.8

conda activate unemployment-env
```

Install package dependencies:

```sh
Navigate to the directory where files are located.

pip install -r requirements.txt
```

## Configuration


[Obtain an API Key](https://www.alphavantage.co/support/#api-key) from AlphaVantage.

Then create a local ".env" file and provide the key like this:

```sh
# this is the ".env" file...

ALPHAVANTAGE_API_KEY="_________"
```


## Usage

Run the unemployment report:

```sh
python -m app.unemployment

python -m app.stocks

## Testing

```sh
pytest

pytest -v # the verbose option shows you all the test names

## Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```