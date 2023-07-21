import pip
import requests
from flask import flask, request, jsonify, make_response, Flask, render_template
import json

app = Flask(__name__)


@app.route('/Date')
def home():
    return render_template('DateTime.html')


@app.route("/Snacks")
def receipt():
    return render_template('Snacks.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
