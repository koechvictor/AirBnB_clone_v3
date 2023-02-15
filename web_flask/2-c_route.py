#!/usr/bin/python3
"""This module runs a flask application server"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_flask():
    """root route returning the desired string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """hbnb route returning the desired string"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """display C and then text"""
    return "C " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
