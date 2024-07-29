#!/usr/bin/python3
"""
A simple Flask Application

This script creates a basic Flask web application that displays
"Hello HBNB!" when accessing the root URL ("/").

Usage:
    - Run the script.
    - Access the root URL ("/") in your web browser to see the message.

Example:
    $ python3 -m web_flask.0-hello_route

Attributes:
    app (Flask): The Flask application object.
"""

from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Root Route Function

    This function defines a route ("/") in a Flask application.

    Attributes:
        strict_slashes (bool): A flag indicating whether to redirect requests
        with trailing slashes to the route without the trailing slash.
        Default is False.

    Returns:
        str: A greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    HBNB Route Function

    This function defines a route ("/hbnb") in a Flask application.

    Attributes:
        strict_slashes (bool): A flag indicating whether to redirect requests
        with trailing slashes to the route without the trailing slash.
        Default is False.

    Returns:
        str: A message "HBNB".
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """
    C Route Function

    This function defines a route ("/c/<text>") in a Flask application.

    Attributes:
        strict_slashes (bool): A flag indicating whether to redirect requests
        with trailing slashes to the route without the trailing slash.
        Default is False.

    Params:
        text: A string that will be concatenated to the result.

    Returns:
        str: A message "C <text>".
    """
    return "C {}".format(escape(text).replace('_', ' '))


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text):
    """
    Python Route Function

    This function defines a route ("/python/<text>") in a Flask application.

    Attributes:
        strict_slashes (bool): A flag indicating whether to redirect requests
        with trailing slashes to the route without the trailing slash.
        Default is False.

    Params:
        text: A string that will be concatenated to the result.

    Returns:
        str: A message "Python <text>".
    """
    return "Python {}".format(escape(text).replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """
    Number Route Function

    This function defines a route ("/number/<int:n>") in a Flask application.

    Attributes:
        strict_slashes (bool): A flag indicating whether to redirect requests
        with trailing slashes to the route without the trailing slash.
        Default is False.

    Params:
        n: An integer that will be concatenated to the result.

    Returns:
        str: A message "<n> is a number".
    """
    return "{} is a number".format(int(escape(n)))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_route(n):
    """
    Number Template Route Function

    This function defines a route ("/number_template/<int:n>")
    in a Flask application.

    Attributes:
        strict_slashes (bool): A flag indicating whether to redirect requests
        with trailing slashes to the route without the trailing slash.
        Default is False.

    Params:
        n: An integer that will be concatenated to the result.

    Returns:
        A html page with a message "<n> is a number" inside H1 tag.
    """
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even_route(n):
    """
    Number Odd or Even Route Function

    This function defines a route ("/number_odd_or_even/<int:n>")
    in a Flask application.

    Attributes:
        strict_slashes (bool): A flag indicating whether to redirect requests
        with trailing slashes to the route without the trailing slash.
        Default is False.

    Params:
        n: An integer that will be concatenated to the result.

    Returns:
        A html page with a message "<n> is a even | odd" inside H1 tag.
    """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
