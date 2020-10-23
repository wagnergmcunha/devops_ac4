import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')

def fibon():
    p = 1
    a = 0
    r = "0,"

    for i in range(51):
        tmp = p
        p = p + a
        a = tmp
        r += str(p) + ","
    return r

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
