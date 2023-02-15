#!/usr/bin/python3
"""This module runs the flask application server"""

from flask import Flask, escape, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def hello_states():
    """display template with states"""
    states = []
    for k, v in storage.all().items():
        if k.split(".")[0] == 'State':
            states.append(v)
    states.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
