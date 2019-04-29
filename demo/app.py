#!/usr/bin/python3
# -*- coding: utf-8 -*
# __author__ = 'Zhang Shi Qiang'
from flask import Flask, request, redirect, url_for, abort, make_response

app = Flask(__name__)


@app.before_first_request
def one_fw():
    str1 = "one"
    print(str1)


@app.before_request
def first_fw():
    print('首次请求')


@app.route('/')
def index():
    return '<h1> Hello Flask! </h1>'


@app.route('/set/<name>')
def set_cookie(name):
    response = make_response(redirect(url_for('say_hello')))
    response.set_cookie('name', name)
    return response


@app.route('/hi')
@app.route('/hello')
def say_hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name','Flask')
    return '<h1>Hello, %s! </h1>' % name


@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello , %s</h1>' % name


@app.route('/goback/<int:year>')
def go_back(year):
    return '<h3>Welcome to %d !</h3>' % (2019 - year)


@app.route('/colors/<any(blue,white,red):color>')
def colors(color):
    return '<p>Love is %s</p>' % color


'''
@app.after_request
def af_fw():
    print('正常请求结束')



@app.teardown_request
def td_fw():
    print('请求结束！')
'''


@app.route('/testurl')
def test_url():
    return redirect(url_for('say_hello'))


@app.route('/brew/<drink>')
def teapot(drink):
    if drink == 'coffee':
        abort(418)
    else:
        return 'A drop of tea.'


@app.route('/note/<any(text,html,xml,json):t_types>')
def note_type(t_types):
    data ={
        'name':'Cola Zhang',
        'gender':'male'
    }
    data1 = 'name: Coal zhang, gender:male'
    if t_types == 'json':
        '''
        from flask import json
        response = make_response(json.dumps(data))
        response.minitpye = 'application/json'
        return response
        '''
        from flask import jsonify
        return jsonify(data)

    if t_types == 'xml':
        pass

    if t_types == 'text':
        response = make_response(data1)
        response.minitpye = 'text/plain'
        return response

    if t_types == 'html':
        pass

    else:
        return '输入错误'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
