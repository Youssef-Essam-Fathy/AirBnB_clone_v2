#!/usr/bin/python3
''' a script to start the Flask web application'''
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_hbnb():
    '''Function returns hello statement'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    '''Function returns HBNB statement'''
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    '''Function returns HBNB statement'''
    text = text.replace('_', ' ')
    return 'c {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
