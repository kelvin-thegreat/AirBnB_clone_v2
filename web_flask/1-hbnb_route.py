#!/usr/bin/python3
"""Script that starts Flask web application
Routes:- / - display "Hello HBNB!"
           - /hbnb - display "HBNB"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_route():
    """Outputs Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """outputs HBNB"""
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
