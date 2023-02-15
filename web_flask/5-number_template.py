#!/usr/bin/python3
"""This module runs the flask application server"""

from flask import Flask, escape, render_template
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


@app.route('/python/', defaults={"text": "is_cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text):
    """display Python and then text"""
    return "Python %s" % escape(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def hello_number(n):
    """display n if number and then text"""
    return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def hello_template(n):
    """display template if n is a number"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
