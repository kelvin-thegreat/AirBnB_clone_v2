#!/usr/bin/python3
"""Starts Flask web application
Routes:
    / - Display "Hello HBNB!"
    /hbnb - Display "HBNB"
    /c/<text> - Display "C " followed by the value of the text variable (replace underscore _ symbols with a space)
    /python/<text> - Display "Python " followed by the value of the text variable (replace underscore _ symbols with a space)
    /number/<n> - Display n if it is an integer
    /number_template/<n> - Display an HTML page if n is an integer
    /number_odd_or_even/<n> - Display if a number is odd or even
"""

from flask import Flask, render_template

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Display an HTML page if n is an integer."""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Display if a number is odd or even."""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")

