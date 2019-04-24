#!/usr/bin/python3
# -*- coding: utf-8 -*
# __author__ = 'Zhang Shi Qiang'
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> Hello Flask! </h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
