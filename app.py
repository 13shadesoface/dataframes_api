from flask import Flask, jsonify
import json
#import pandas
app = Flask(__name__)



@app.route('/health')
def check_health():
    return 'healthy'


@app.route("/compute", methods=["GET", "POST"])
def compute():
    dct = {
        "blabla": 42,
        "blablabla": "bla"
    }
    return dct


@app.route("/compute/group_by", methods=["POST"])
def group_by():
    dct = {
        "blabla": 42,
        "blablabla": "bla"
    }
    return dct

@app.route("/compute/non_null", methods=["POST"])
def non_null():
    dct = {
        "blabla": 42,
        "blablabla": "bla"
    }
    return dct


@app.route("/compute/stats", methods=["POST"])
def stats():
    dct = {
        "blabla": 42,
        "blablabla": "bla"
    }
    return dct


if __name__ == '__main__':
    app.run()
