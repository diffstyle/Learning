#!/usr/bin/python3
# -*- coding: utf-8 -*
# __author__ = 'Zhang Shi Qiang'
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> Hello Flask! </h1>'


@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hello, Flask ! </h1>'


@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello , %s</h1>' % name


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
