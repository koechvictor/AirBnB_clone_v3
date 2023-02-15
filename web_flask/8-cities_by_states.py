#!/usr/bin/python3
"""This module runs the flask application server"""

from flask import Flask, escape, render_template
from models import storage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def hello_cities():
    """display template with states"""
    states = []
    for k, v in storage.all().items():
        if k.split(".")[0] == 'State':
            states.append(v)
    states.sort(key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def hello_goodbye(exc):
    """close the storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
