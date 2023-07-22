#!/usr/bin/python3
"""Starts Flask web app
Routes:
    / - Display "Hello HBNB!"
    /hbnb - Display "HBNB"
    /c/<text> - Display "C <text>"
    /python/<text> - Display "Python is cool"
    /number/<n> - Display n if it is an integer
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_route():
    """Display "Hello HBNB!" """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display "HBNB" """
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def c_text(text):
    """Display 'C' followed by <text> content."""
    text = text.replace("_", " ")
    return "C %s" % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_text(text="is cool"):
    """Display 'Python' followed by <text> content (default: 'is cool')."""
    text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """Display n if it is an integer."""
    return "%i is a number" % n


if __name__ == "__main__":
    app.run(host="0.0.0.0")

