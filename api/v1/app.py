#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask
from models import storage
from os import getenv
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close():
    """Calls storage close method"""
    storage.close()

if __name__ == '__main__':
    if getenv("HBNB_API_HOST"):
        host = getenv("HBNB_API_HOST")
    else:
        host = '0.0.0.0'
    if getenv("HBNB_API_PORT"):
        port = getenv("HBNB_API_PORT")
    else:
        port = '5000'
    app.run(host=host, port=port, threaded=True)