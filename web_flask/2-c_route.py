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

from flask import Flask
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
