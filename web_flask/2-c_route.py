#!/usr/bin/python3
"""Script that tarts Flask web application
with Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
    /c/<text> - display "C <text>"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_route():
    """outputs or prints Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """outputs/prints HBNB"""
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """prints C then <text> content"""
    text = text.replace("_", " ")
    return "C %s" % text


if __name__ == "__main__":
    app.run(host="0.0.0.0")
