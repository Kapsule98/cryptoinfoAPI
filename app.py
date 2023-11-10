from flask import Flask
from flask.globals import session
from flask.json import jsonify
from flask_cors import CORS
from flask import jsonify
from requests import Request, Session
import json
import os

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return {"msg":"Index"},200

@app.route('/cryptolist')
def getCrypto():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': os.environ.get("CMC_PRO_API_KEY"),
    }
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url)
        data = json.loads(response.text)
        return data,200
    except Exception as e:
        return "something went wrong",500

@app.route('/crypto/<string:id>')
def getCoin(id):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?id=' + id
    print(url)
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': os.environ.get("CMC_PRO_API_KEY"),
    }
    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url)
        data = json.loads(response.text)
        return data,200
    except Exception as e:
        return "something went wrong",500


if __name__ == "__main__":
    app.run(debug=True)
